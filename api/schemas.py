from marshmallow import fields, Schema

from app import ma
from api.models import User, Folder, Note, NoteItem


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        fields = ['name', 'username', 'password']


class VerifyPostSchema(Schema):
    username = fields.String(required=True)


class FolderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Folder
        load_instance = True
        fields = ['id', 'name']


class NoteSchema(ma.SQLAlchemySchema):
    items = fields.Nested('NoteItemSchema', many=True)

    class Meta:
        model = Note
        load_instance = True
        fields = ['id', 'name', 'folder_id', 'type', 'is_public', 'items']


class NoteItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = NoteItem
        load_instance = True
        fields = ['id', 'text_body']


class NotePagingSchema(Schema):
    has_next = fields.Boolean()
    has_prev = fields.Boolean()
    items = fields.Nested('NoteSchema', many=True)
    next_num = fields.Integer()
    pages = fields.Integer()
    per_page = fields.Integer()
    prev_num = fields.Integer()
    total = fields.Integer()
