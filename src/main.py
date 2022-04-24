__author__ = {'name': ('David Serrano', 'Jesús David Nieves'),
              'code': ('T00061734', 'T00058742')}

from flask import Flask, render_template, request, redirect, flash
from config import config


app = Flask(__name__)


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def register():
    return render_template('register.html')


@app.route('/projects')
def projects():
    return "Página en construcción"


if __name__ == '__main__':
    app.config.from_object(config['dev'])
    app.run(debug=True, port=5000, host='0.0.0.0')
