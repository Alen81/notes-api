from flask_restx import fields


def signup(api):
    return api.model(
        'signup', {
            'name': fields.String,
            'username': fields.String,
        }
    )


def signup_post(api):
    return api.model(
        'signup_post', {
            'name': fields.String,
            'username': fields.String,
            'password': fields.String,
        }
    )


def verify_post(api):
    return api.model(
        'verify_post', {
            'username': fields.String,
        }
    )


def folder(api):
    return api.model(
        'folder', {
            'id': fields.Integer,
            'name': fields.String,
        }
    )


def folder_post(api):
    return api.model(
        'folder_post', {
            'name': fields.String,
        }
    )


def note_item(api):
    return api.model(
        'note_item', {
            'id': fields.Integer,
            'text_body': fields.String,
        }
    )


def note(api):
    return api.model(
        'note', {
            'id': fields.Integer,
            'name': fields.String,
            'folder_id': fields.Integer,
            'type': fields.Integer,
            'is_public': fields.Boolean,
            'items': fields.List(fields.Nested(note_item(api)))
        }
    )


def note_paging(api):
    return api.model(
        'note_paging', {
            'has_next': fields.Boolean,
            'has_prev': fields.Boolean,
            'items': fields.List(fields.Nested(note(api))),
            'next_num': fields.Integer,
            'pages': fields.Integer,
            'per_page': fields.Integer,
            'prev_num': fields.Integer,
            'total': fields.Integer,
        }
    )


def note_item_post(api):
    return api.model(
        'note_item_post', {
            'text_body': fields.String,
        }
    )


def note_post(api):
    return api.model(
        'note_post', {
            'name': fields.String,
            'folder_id': fields.Integer,
            'type': fields.Integer,
            'is_public': fields.Boolean,
            'items': fields.List(fields.Nested(note_item_post(api)))
        }
    )
