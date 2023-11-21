from db import db
from enum import Enum
from sqlalchemy import Enum as EnumType

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)


class JobApplicationStatus(Enum):
    APPLIED = 'APPLIED'
    INTERVIEWED = 'INTERVIEWED'
    REJECTED = 'REJECTED'
    OFFER_ACCEPTED = 'OFFER_ACCEPTED'


class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    user = db.relationship('User', backref=db.backref("job_applications", lazy=True))
    job = db.relationship('Job', backref=db.backref("applications", lazy=True))
    status = db.Column(EnumType(JobApplicationStatus), default=JobApplicationStatus.APPLIED, nullable=False) 