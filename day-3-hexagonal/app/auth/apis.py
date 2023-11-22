from flask import Blueprint, request
from app.common.bcrypt import bcrypt
from infrastructure.user.models import User
from infrastructure.db import db
import jwt, os
from datetime import datetime, timedelta
from marshmallow import Schema, fields, ValidationError
from core.auth.services import AuthService
from app.di import injector

auth_blp = Blueprint("auth", __name__)
auth_service = injector.get(AuthService)

class UserRegistrationSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)

@auth_blp.route("/registration", methods=["POST"])
def register():
    data = request.get_json()
    schema = UserRegistrationSchema()
    try:
        data = schema.load(data)
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    result = auth_service.register(
        username=data['username'],
        password=data['password'],
        email=data['email']
    )
    
    return result


@auth_blp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    result = auth_service.login(
        username=username,
        password=password
    )

    return result
