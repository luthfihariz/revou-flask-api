import os
from flask import Flask
from task.apis import task_blueprint
from event.apis import event_blueprint
from user.apis import user_blueprint
from db import db

app = Flask(__name__)
database_url = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db.init_app(app)

app.register_blueprint(task_blueprint, url_prefix="/tasks")
app.register_blueprint(event_blueprint, url_prefix="/events")
app.register_blueprint(user_blueprint, url_prefix="/users")

# with app.app_context():
#     db_init()