from http import HTTPStatus

from flask import Flask, config
from flask import Response
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restx import Api
from marshmallow import ValidationError

from api.db_store import db
from api.utils import format_error
import config

# app
app = Flask(__name__)
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Swagger
authorizations = {
    "basic_auth": {
        "type": "basic",
        "in": "header",
        "name": "x-access-token"
    }
}
api = Api(
    app,
    version='1.0',
    title='Notes API',
    description="Manage your notes in a simple way.",
    doc='/',
    authorizations=authorizations,
    security='basic',
)

# namespaces
from api.auth import api as auth_ns  # noqa
from api.folder import api as folder_ns  # noqa
from api.note import api as note_ns  # noqa
api.add_namespace(auth_ns)
api.add_namespace(folder_ns)
api.add_namespace(note_ns)


# error handling
@app.errorhandler(Exception)
def handle_exception(error):
    return Response(
        'Ups, something went wrong.', HTTPStatus.INTERNAL_SERVER_ERROR)


@app.errorhandler(ValidationError)
def handle_exception(error):
    return Response(format_error(error.messages), HTTPStatus.BAD_REQUEST)
