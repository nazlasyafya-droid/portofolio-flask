from flask import Flask, render_template, request, redirect, url_for, session
from extensions import db
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ganti-dengan-kunci-rahasia-anda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB

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
    return "Halaman Portofolio (belum jadi)"

@app.route('/contact')
def contact():
    return "Halaman Kontak (belum jadi)"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)