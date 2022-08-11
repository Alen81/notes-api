import base64
from functools import wraps

from flask import request
from werkzeug.security import check_password_hash
from werkzeug.exceptions import Unauthorized

from api.models import User


def encode_credentials(username: str, password: str) -> str:
    return base64.b64encode(f'{username}:{password}'.encode()).decode()


def verify_credentials(username: str, password: str) -> User | None:
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def get_user_from_credentials(credentials: str) -> User | None:
    decoded = base64.b64decode(credentials).decode("utf-8")
    user_and_pass = decoded.split(':')
    username = user_and_pass[0]
    password = user_and_pass[1]
    user = verify_credentials(username, password)
    return user


def credentials_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        credentials = None
        if "authorization" in request.headers:
            credentials = request.headers["authorization"].split(" ")[1]
        if not credentials:
            raise Unauthorized('Authentication credentials are missing!')

        user = get_user_from_credentials(credentials)
        if not user:
            raise Unauthorized('Invalid authentication credentials!')

        return func(*args, user, **kwargs)
    return decorated


def credentials_optional(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        credentials = None
        if "authorization" in request.headers:
            credentials = request.headers["authorization"].split(" ")[1]

        user = None
        if credentials:
            user = get_user_from_credentials(credentials)
            if not user:
                raise Unauthorized('Invalid authentication credentials!')

        return func(*args, user, **kwargs)
    return decorated
