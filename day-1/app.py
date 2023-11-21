from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/")
def index():
    base_url = request.base_url
    args = request.args
    endpoint = request.endpoint
    http_method = request.method

    return {
        'base_url': base_url,
        'args': args,
        'endpoint': endpoint,
        'http_method': http_method
    }

@app.route("/error")
def error():
    return {"error": "Username dan password tidak sesuai!"}, 401


# GET /books -> return list of books
# POST /books -> add a book to the list
# GET /books/<int:book_id> -> return a book

books = []

@app.route("/books", methods=["GET", "POST"])
def get_book_list():
    if request.method == "GET":    
        return books
    
    title = request.form.get("title")
    author = request.form.get("author")

    books.append({
        'title': title,
        'author': author
    })

    return books

@app.route("/books/<int:index>", methods=["GET"])
def get_a_book(index):
    if index > len(books):
        return {"error": "Buku tidak ditemukan!"}, 404

    return books[index - 1]


news = []

# GET /news -> return news list
# POST /news -> create a news
# GET /news/<int:index> -> return a news
# DELETE /news/<int:index> -> delete a news

@app.route("/news", methods=["GET"])
def get_news():
    return news

@app.route("/news", methods=["POST"])
def create_news():
    title = request.form.get("title")
    content = request.form.get("content")

    news.append({
        'title': title,
        'content': content
    })

    return news

@app.route("/news/<int:index>", methods=["GET"])
def get_single_news(index):
    if index > len(news):
        return {"error": "news not found!"}, 404
    
    return news[index - 1]


@app.route("/news/<int:index>", methods=["DELETE"])
def delete_news(index):
    if index > len(news):
        return {"error": "news not found!"}, 404
    
    del news[index - 1]

    return news;


# Task management
# GET /tasks -> return tasks list
# POST /tasks -> create task with json
# PUT /tasks -> update task with json
# DELETE /task -> delete task with json


tasks = [{'task': 'Coding with Flask', 'status': 'in progress'}]

@app.route("/tasks", methods=["GET"])
def get_tasks_list():
    return tasks

@app.route("/tasks", methods=["POST"])
def create_tasks():
    # check json or not
    if not request.is_json:
        return {"error": "Bukan json!!"}, 400

    data = request.get_json()
    
    # task available in data or not
    if "task" not in data:
        return {"error": "Task not available"}, 400
    
    task = data.get("task")
    
    tasks.append({
        'task': task,
        'status': 'to do'
    })

    return tasks

allowed_status = ["in progress", "to do", "done"]

@app.route("/tasks/<int:index>", methods=["PUT"])
def update_tasks(index):
    if index > len(tasks):
        return {"error": "task not found!"}, 404
    
    if status not in allowed_status:
        return {"error": "status tidak valid!"}, 400
    
    data = request.get_json()
    task = data.get("task")
    status = data.get("status") # None

    updated_task = tasks[index - 1]

    if task:
        updated_task["task"] = task
    
    if status:
        updated_task["status"] = status

    tasks[index - 1] = updated_task

    return tasks


@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if index > len(tasks):
        return {"error": "news not found!"}, 404
    
    del tasks[index - 1]

    return tasks