import json
from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource
from sqlalchemy import desc
from werkzeug.exceptions import BadRequest, NotFound, Forbidden

from app import db
from api.auth_basic import credentials_required, credentials_optional
from api.utils import get_three_state_bool
from api.models import Folder, Note, NoteItem, NoteType, User
from api.schemas import NoteSchema, NotePagingSchema
import api.schemas_doc as schemas_doc

MAX_PER_PAGE = 100
PER_PAGE = 10

api = Namespace('note', description='Manage your notes.', path='/')

note_schema = NoteSchema()
note_schemas = NoteSchema(many=True)
note_paging_schema = NotePagingSchema()

# Fix: Nessted schema, inherit session from the parent
# https://github.com/marshmallow-code/marshmallow/issues/658
note_schema.fields['items'].schema.session = db.session


def note_validation(note: Note):
    if note.type not in NoteType.list():
        raise BadRequest(f'Invalid note type {note.type}.')

    if (note.type == NoteType.SINGLE.value
       and len(note.items) != 1):
        raise BadRequest(
            f'Note with a single note type must have one note.')


@api.route('/note')
class NoteView(Resource):
    @credentials_optional
    @api.doc(security='basic_auth')
    @api.marshal_with(schemas_doc.note_paging(api))
    @api.param(
        'folderid',
        type=int,
        description='Filter by specific folder.'
    )
    @api.param(
        'ispublic',
        type=str,
        description="""Public or private visibility. [true, false]
        When not specified user can see all of his notes, either private
        or public."""
    )
    @api.param(
        'notetext',
        type=str,
        description='Search for text in notes.'
    )
    @api.param(
        'sort',
        type=str,
        description='Sort by possible options. [shared, heading]'
    )
    @api.param(
        'sortdesc',
        type=str,
        description='Turn on descending order. [true, false]'
    )
    @api.param(
        'page',
        type=int,
        description='Show specific page.'
    )
    @api.param(
        'perpage',
        type=int,
        description='Show specific number of items per page.'
    )
    def get(self, user: User):
        folder_id = request.args.get("folderid", default=None, type=int)
        is_public_param = request.args.get("ispublic", default=None, type=str)
        note_text = request.args.get("notetext", default=None, type=str)
        sort = request.args.get("sort", default=None, type=str)
        sort_desc_param = request.args.get(
            "sortdesc", default='false', type=str)
        page = request.args.get("page", default=1, type=int)
        perpage = request.args.get("perpage", default=PER_PAGE, type=int)

        if user:
            is_public = get_three_state_bool(is_public_param)
        else:
            is_public = True

        sort_desc = False
        if sort_desc_param.lower() == 'true':
            sort_desc = True

        filters = []
        if folder_id:
            filters.append(Folder.id == folder_id)

        if is_public is True:
            filters.append(Note.is_public == True)  # noqa
        elif is_public is False:
            filters.append(Folder.user_id == user.id)
            filters.append(Note.is_public == False)  # noqa
        elif is_public is None:
            filters.append(Folder.user_id == user.id)

        if note_text:
            subquery = db.session.query(NoteItem.note_id) \
                .filter(NoteItem.text_body.contains(note_text)) \
                .group_by(NoteItem.note_id) \
                .subquery()
            filters.append(Note.id.in_(subquery))

        order = None
        if sort and sort == 'heading':
            order = Note.name
        if sort and sort == 'shared':
            order = Note.is_public

        if order and sort_desc:
            order = desc(order)

        notes = db.session.query(Note).outerjoin(Folder) \
            .filter(*filters) \
            .order_by(order) \
            .paginate(
                page=page,
                per_page=perpage,
                error_out=True,
                max_per_page=MAX_PER_PAGE
            )

        return note_paging_schema.dump(notes)


@api.route('/folder/<int:folder_id>/note')
class FolderNoteView(Resource):
    @credentials_required
    @api.doc(security='basic_auth')
    @api.expect(schemas_doc.note_post(api))
    @api.marshal_with(schemas_doc.note(api))
    def post(self, user: User, folder_id: int):
        folder = Folder.query.get(folder_id)
        if not folder:
            raise NotFound('Folder not found.')
        if folder.user_id != user.id:
            raise Forbidden(
                'Not authorized for adding notes to this folder.')

        data = json.loads(request.data)
        note = note_schema.load(data, session=db.session)

        note_validation(note)

        if note.folder_id != folder_id:
            raise BadRequest('Inconsistent folder id.')

        note_exist = Note.query.filter_by(
            name=note.name, folder_id=folder_id).first()
        if note_exist:
            raise BadRequest(
                'There is already a note in the folder with this name.')

        db.session.add(folder)
        note.folder = folder
        db.session.add(note)
        db.session.commit()

        return note_schema.dump(note), HTTPStatus.CREATED


@api.route('/note/<int:id>')
class NoteIdView(Resource):
    @credentials_required
    @api.doc(security='basic_auth')
    @api.expect(schemas_doc.note(api))
    @api.marshal_with(schemas_doc.note(api))
    def put(self, user: User, id: int):
        note = Note.query.get(id)
        if not note:
            raise NotFound('Note not found.')
        if note.folder.user_id != user.id:
            raise Forbidden('Not authorized for changing this note.')
        folder_id = note.folder_id
        item_ids = [item.id for item in note.items]

        data = json.loads(request.data)
        note_update = note_schema.load(data, session=db.session)

        note_validation(note_update)

        if note_update.id and note_update.id != id:
            raise BadRequest('Inconsistent id.')
        if note_update.folder_id and note_update.folder_id != folder_id:
            raise BadRequest('Inconsistent folder id.')

        for item_update in note_update.items:
            if item_update.id and item_update.id not in item_ids:
                raise BadRequest(
                    f"Can't update item with id {item_update.id}.")

        note_exist = Note.query \
            .filter(
                Note.name == note_update.name,
                Note.id != id,
                Note.folder_id == folder_id
            ).first()
        if note_exist:
            raise BadRequest('You already have a folder with this name.')

        db.session.add(note_update)
        db.session.commit()

        return note_schema.dump(note_update)

    @credentials_required
    @api.doc(security='basic_auth')
    def delete(self, user: User, id: int):
        note = Note.query.get(id)
        if not note:
            raise NotFound('Note not found.')
        if note.folder.user_id != user.id:
            raise Forbidden('Not authorized for removing this note.')

        db.session.delete(note)
        db.session.commit()

        return None, HTTPStatus.NO_CONTENT
