from flask import Flask, render_template, request, redirect, url_for, session
from extensions import db
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ganti-dengan-kunci-rahasia-anda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB
app.config['ADMIN_USERNAME'] = 'admin'
app.config['ADMIN_PASSWORD'] = 'xxx1515'

db.init_app(app)

from models import Project, Message, Profile, Skill

@app.route('/')
def index():
    profile = Profile.query.first()
    return render_template('index.html', profile=profile)

@app.route('/about')
def about():
    profile = Profile.query.first()
    skills = Skill.query.all()
    return render_template('about.html', profile=profile, skills=skills)

@app.route('/portfolio')
def portfolio():
    projects = Project.query.all()
    return render_template('portofolio.html', projects=projects)

@app.route('/portfolio/<int:id>')
def project_detail(id):
    project = Project.query.get_or_404(id)
    return render_template('project_detail.html', project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    profile = Profile.query.first()
    success = False

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_text = request.form.get('message')

        new_message = Message(name=name, email=email, message=message_text)
        db.session.add(new_message)
        db.session.commit()
        success = True

    return render_template('contact.html', profile=profile, success=success)

@app.route('/dashboard/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']:
            session['user'] = username
            return redirect(url_for('dashboard_index'))
        else:
            error = "Username atau password salah."

    return render_template('dashboard/login.html', error=error)


@app.route('/dashboard/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard_index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return "Dashboard (belum jadi)"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)