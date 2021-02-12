from flask import Flask, request, jsonify, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


##########
# CONFIG #
##########
# Will probably move to app/__init__.py

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Will probably move inside create_app()
# alongside db/migrate init, importing Task, registering blueprints
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "SQLALCHEMY_DATABASE_URI")

##########
# MODELS #
##########
# Will probably move to app/models.py


class Task(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime)

    def __init__(self, title, description="", completed_at=None):
        self.title = title
        self.description = description
        self.completed_at = completed_at

    def __repr__(self):
        return f'<Task {self.title}>'


###############
# MORE CONFIG #
###############
# Will probably move to app/__init__.py

# db.drop_all()
db.create_all()
db.session.commit()


##########
# ROUTES #
##########
# Will probably be refactored to use Blueprints
# (which replaces @app.route() decorators with @blueprint_name.route())
#
# Will probably move to app/routes.py

@app.route('/')
def index():
    return redirect(url_for('tasks'))


def build_dict_from_task(task):
    is_complete = True if task.completed_at else False
    return {
        "id": task.task_id,
        "title": task.title,
        "description": task.description,
        "is_complete": is_complete
    }


def build_task_from_json(json):
    return Task(title=json["title"], description=json["description"], completed_at=json["completed_at"])


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        tasks = Task.query.all()
        results = []
        for task in tasks:
            results.append(build_dict_from_task(task))
        return jsonify(results)
    elif request.method == 'POST':
        new_task = build_task_from_json(request.get_json())

        db.session.add(new_task)
        db.session.commit()

        return {"tasks": build_dict_from_task(new_task)}


@app.route('/tasks/<task_id>', methods=['GET', 'PUT', 'DELETE'])
def task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'GET':
        return {"task": build_dict_from_task(task)}
    elif request.method == 'PUT':
        form_data = request.get_json()

        task.title = form_data['title']
        task.description = form_data['description']
        task.completed_at = form_data['completed_at']

        db.session.commit()

        return {"task": build_dict_from_task(task)}
    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return {"details": f'Task {task.task_id} "{task.title}" successfully deleted'}


@app.route('/tasks/<task_id>/complete', methods=['PATCH'])
def toggle_complete(task_id):
    task = Task.query.get_or_404(task_id)

    if task.completed_at:
        task.completed_at = None
    else:
        task.completed_at = datetime.utcnow()

    db.session.commit()

    return {"task": build_dict_from_task(task)}
