from app import app

from flask import request, render_template, flash, redirect, url_for

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    
    else:
        word = request.form['word']

        return redirect(url_for('index'))
        