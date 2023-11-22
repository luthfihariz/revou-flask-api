import os
from flask import Flask
from db import db, db_init
from common.bcrypt import bcrypt
from auth.apis import auth_blp
from user.apis import user_blueprint

app = Flask(__name__)

database_url = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(auth_blp, url_prefix="/auth")
app.register_blueprint(user_blueprint, url_prefix="/user")

# with app.app_context():
#     db_init()
