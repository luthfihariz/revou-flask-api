from flask import Blueprint, request
from user.models import User
from db import db

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data["username"]
    email = data["email"]

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return {
        'id': new_user.id
    }