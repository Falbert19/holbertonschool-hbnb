from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/place')
def place():
    return render_template('place.html')

@app.route('/add_review')
def add_review():
    return render_template('add_review.html')

if __name__ == '__main__':
    app.run(debug=True)
