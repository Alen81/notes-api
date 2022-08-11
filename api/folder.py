import json
from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource
from werkzeug.exceptions import BadRequest, NotFound, Forbidden

from app import db
from api.auth_basic import credentials_required
from api.models import Folder, User
from api.schemas import FolderSchema
import api.schemas_doc as schemas_doc

api = Namespace('folder', description='Folder for notes.')

folder_schema = FolderSchema()
folder_schemas = FolderSchema(many=True)


def check_folder_access(folder_id: int, user_id: int) -> Folder:
    folder = Folder.query.get(folder_id)
    if not folder:
        raise NotFound('Folder not found.')
    if folder.user_id != user_id:
        raise Forbidden('Not authorized to access this folder.')

    return folder


@api.route('')
class FolderView(Resource):
    @credentials_required
    @api.doc(security='basic_auth')
    @api.marshal_with(schemas_doc.folder(api), as_list=True)
    def get(self, user: User):
        folders = Folder.query.filter_by(user_id=user.id).all()
        return folder_schemas.dump(folders)

    @credentials_required
    @api.doc(security='basic_auth')
    @api.expect(schemas_doc.folder_post(api))
    @api.marshal_with(schemas_doc.folder(api))
    def post(self, user: User):
        data = json.loads(request.data)
        folder = folder_schema.load(data, session=db.session)

        folder_exist = Folder.query.filter_by(
            name=folder.name, user_id=user.id).first()
        if folder_exist:
            raise BadRequest('You already have a folder with this name.')

        folder.user_id = user.id
        db.session.add(folder)
        db.session.commit()

        return folder_schema.dump(folder), HTTPStatus.CREATED


@api.route('/<int:id>')
class FolderIdView(Resource):
    @credentials_required
    @api.doc(security='basic_auth')
    @api.expect(schemas_doc.folder_post(api))
    @api.marshal_with(schemas_doc.folder(api))
    def put(self, user: User, id: int):
        folder = check_folder_access(id, user.id)

        data = json.loads(request.data)
        folder_update = folder_schema.load(
            data, session=db.session, instance=folder)

        if folder.id != id:
            raise BadRequest('Inconsistent id.')

        folder_exist = Folder.query.filter(
            Folder.name == folder.name,
            Folder.id != id,
            Folder.user_id == user.id
        ).first()
        if folder_exist:
            raise BadRequest('You already have a folder with this name.')

        db.session.add(folder_update)
        db.session.commit()

        return folder_schema.dump(folder_update)

    @credentials_required
    @api.doc(security='basic_auth')
    def delete(self, user: User, id: int):
        folder = check_folder_access(id, user.id)

        db.session.delete(folder)
        db.session.commit()

        return None, HTTPStatus.NO_CONTENT
