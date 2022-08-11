import json
from http import HTTPStatus

from flask import request
from flask_restx import Namespace
from flask_restx import Namespace, Resource

from werkzeug.security import generate_password_hash
from werkzeug.exceptions import BadRequest

from app import db
from api.models import User
from api.auth_basic import credentials_required
from api.schemas import UserSchema, VerifyPostSchema
import api.schemas_doc as schemas_doc

api = Namespace('auth', description='Authentication.')

user_schema = UserSchema()
verify_post_schema = VerifyPostSchema()


@api.route('/signup')
class SignupView(Resource):
    @api.expect(schemas_doc.signup_post(api))
    @api.marshal_with(schemas_doc.signup(api))
    def post(self):
        data = json.loads(request.data)
        user = user_schema.load(data, session=db.session)

        user_exist = User.query.filter_by(username=user.username).first()
        if user_exist:
            raise BadRequest('User name is already taken.')

        user.password = generate_password_hash(user.password, method='sha256')
        db.session.add(user)
        db.session.commit()

        response = user_schema.dump(user)
        response.pop('password')
        return response


@api.route('/verify')
class VerifyView(Resource):
    @credentials_required
    @api.doc(security='basic_auth')
    @api.expect(schemas_doc.verify_post(api))
    def post(self, user: User):
        data = json.loads(request.data)
        verify_post_schema.load(data)

        if user.username == data['username']:
            return {}, HTTPStatus.OK
        return {}, HTTPStatus.UNAUTHORIZED
