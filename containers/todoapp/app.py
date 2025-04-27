from flask import Flask, render_template, redirect, url_for, request, flash
import logging
import time
import psutil  # Import psutil to capture app-level metrics
from threading import Thread
from models import db, Task
from config import Config
from datetime import datetime
from prometheus_client import Counter, generate_latest, Summary
import pymysql
import os

pymysql.install_as_MySQLdb()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)  

# Initialize the database
db.init_app(app)

# Configure logging to produce logs for Promtail
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# file_handler = logging.FileHandler('app.log')
# file_handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# Metrics tracking variables
tasks_created = 0
tasks_completed = 0
tasks_deleted = 0
task_creation_times = []  # To track how long tasks take to complete

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global tasks_created
    title = request.form.get('title')
    description = request.form.get('description')

    if not title:
        flash('Title is required.')
        return redirect(url_for('index'))

    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()

    tasks_created += 1

    log_message = f"Task '{title}' created successfully."
    logger.info(log_message)

    flash('Task created successfully!')
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>', methods=['GET', 'POST'])
def task(task_id):
    global tasks_completed
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.completed = 'completed' in request.form

        db.session.commit()

        if task.completed:
            tasks_completed += 1
            task_creation_times.append(time.time() - task.timestamp)

        log_message = f"Task {task_id} updated successfully."
        logger.info(log_message)

        flash('Task updated successfully!')
        return redirect(url_for('index'))

    return render_template('task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks_deleted
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()

    tasks_deleted += 1

    log_message = f"Task {task_id} deleted successfully."
    logger.info(log_message)

    flash('Task deleted successfully!')
    return redirect(url_for('index'))

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.errorhandler(Exception)
def handle_exception(e):
    log_message = f"An error occurred: {str(e)}"
    logger.error(log_message)

    flash('An internal error occurred.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
