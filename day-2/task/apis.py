from flask import Blueprint, request
from task.models import Task
from user.models import User
from db import db

task_blueprint = Blueprint('task', __name__)

@task_blueprint.route("", methods=["POST"])
def create_tasks():
    # check json or not
    if not request.is_json:
        return {"error": "Bukan json!!"}, 400

    data = request.get_json()
    
    # task available in data or not
    if "title" not in data:
        return {"error": "Title not available"}, 400
    
    title = data.get("title")
    user_id = data.get("user_id")

    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found!"}, 404
    
    task = Task(user=user, title=title)
    db.session.add(task)
    db.session.commit()

    return {"message": "success"}

# tasks = [{'task': 'Coding with Flask', 'status': 'in progress'}]

# @task_blueprint.route("", methods=["GET"])
# def get_tasks_list():
#     return tasks

# allowed_status = ["in progress", "to do", "done"]

# @task_blueprint.route("/<int:index>", methods=["PUT"])
# def update_tasks(index):
#     if index > len(tasks):
#         return {"error": "task not found!"}, 404
    
#     data = request.get_json()
#     task = data.get("task")
#     status = data.get("status") # None
    
#     if status not in allowed_status:
#         return {"error": "status tidak valid!"}, 400            

#     updated_task = tasks[index - 1]

#     if task:
#         updated_task["task"] = task
    
#     if status:
#         updated_task["status"] = status

#     tasks[index - 1] = updated_task

#     return tasks


# @task_blueprint.route("/<int:index>", methods=["DELETE"])
# def delete_task(index):
#     if index > len(tasks):
#         return {"error": "news not found!"}, 404
    
#     del tasks[index - 1]

#     return tasks