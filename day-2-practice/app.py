import os
from flask import Flask
from db import db

app = Flask(__name__)
database_url = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db.init_app(app)


# API Design
# POST /user -> create user
# POST /job -> create job
# POST /job/application -> apply to a job
# PUT /job/application/<job_application_id> -> update job status
# GET /job/application/<job_application_id> -> get job application detail

# Database Design
# Table
# User (id, email, username)
# Job (id, employer, name, description)
# JobApplication (id, user_id, job_id, status)
