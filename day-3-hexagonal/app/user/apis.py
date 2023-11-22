from core.user.services import UserService
from flask import Blueprint, request
from infrastructure.user.models import User
from app.auth.utils import decode_jwt
from app.di import injector

user_blueprint = Blueprint("user", __name__)
user_service = injector.get(UserService)

@user_blueprint.route("/", methods=["GET"])
def get_user_profile():
    payload = decode_jwt(request.headers.get('Authorization'))
    if not payload:
        return {"error": "Token is not valid!"}, 401

    user_id = payload["user_id"]
    result = user_service.get_by_id(user_id)

    if not result:
        return {"error": "User not found!"}, 404
    
    return {
        'id': result.id,
        'username': result.username,
        'email': result.email
    }