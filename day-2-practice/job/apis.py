from flask import Blueprint, request
from job.models import Job, JobApplication
from db import db 
from sqlalchemy.orm import joinedload

job_blueprint = Blueprint("job", __name__)


@job_blueprint.route("", methods=["POST"])
def create_job():
    pass


@job_blueprint.route("/application", methods=["POST"])
def apply_job():
    pass

@job_blueprint.route("/application/<int:job_application_id>", methods=["PUT"])
def update_job_application(job_application_id):
    job_application = JobApplication.query.get(job_application_id)
    if not job_application:
        return {"error": "Job application not found!"}, 404
    
    status = request.get_json().get("status")

    job_application.status = status
    db.session.commit();



@job_blueprint.route("/application/<int:job_application_id>", methods=["GET"])
def get_job_application_detail(job_application_id):
    job_application = JobApplication.query.options(
        joinedload(JobApplication.user), joinedload(JobApplication.job)
    ).filter_by(id=job_application_id).first()

    return job_application