from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ganti-dengan-kunci-rahasia-anda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Halo, Flask berhasil jalan!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)