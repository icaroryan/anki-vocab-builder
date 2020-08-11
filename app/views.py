from app import app

from flask import request, render_template, flash, redirect, url_for

# from urllib.parse import unquote
# import re

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":

        word = request.form["word"]

        return redirect(url_for("search", word=word))
        
    return render_template("index.html")
    

@app.route('/<word>')
def search(word):

    return render_template("index.html", word=word)