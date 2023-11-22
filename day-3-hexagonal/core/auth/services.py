from injector import inject
from core.auth.ports import IUserAccessor
from app.common.bcrypt import bcrypt
from datetime import datetime, timedelta
import jwt,os

class AuthService():
    
    @inject
    def __init__(self, user_accessor: IUserAccessor) -> None:
        self.user_accessor = user_accessor    
    
    def register(self, username: str, password: str, email: str):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user_domain = self.user_accessor.create(
            username=username,
            email=email,
            hashed_password=hashed_password
        )

        return {
            'id': user_domain.id,
            'username': user_domain.username,
        }
                

    def login(self, username: str, password: str):
        user = self.user_accessor.get_by_username(username=username)
        if not user:
            return {"error": "User or password is not valid"}, 400
        
        valid_password = bcrypt.check_password_hash(user.password, password)
        if not valid_password:
            return {"error": "User or password is not valid"}, 400
        
        payload = {
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(minutes=1)
        }
        token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm="HS256")
        
        return {
            'id': user.id,
            'username': user.username,
            'token': token
        }