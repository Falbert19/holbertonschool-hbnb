from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__, template_folder='templates', static_folder='static', static_url_path='/static')

@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/login')
def login():
    return render_template('login.html')

@frontend.route('/place')
def place():
    return render_template('place.html')

@frontend.route('/add_review')
def add_review():
    return render_template('add_review.html')
