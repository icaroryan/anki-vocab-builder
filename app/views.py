from app import app

from flask import request, render_template, flash, redirect, url_for

# from urllib.parse import unquote
# import re

# dictionaries = [
#     {'name': 'Cambridge Dictionary', 'id': 'cambridge', 'url': 'https://dictionary.cambridge.org/us/search/direct/?datasetsearch=english&q={{ word }}', 'x-frame-bypass': False},
#     {'name': 'Longman Dictionary', 'id': 'longman', 'url': 'https://www.ldoceonline.com/search/english/direct/?datasetsearch=english&q={{ word }}', 'x-frame-bypass': True},
#     {'name': 'Thesaurus Synonyms', 'id': 'thesaurus', 'url': 'https://www.thesaurus.com/browse/{{ word }}', 'x-frame-bypass': False},
#     {'name': 'DuckDuckGo Images', 'id': 'duckduckgo', 'url': 'https://duckduckgo.com/?q={{ word }}&iax=images&ia=images', 'x-frame-bypass': True},
#     {'name': 'Sentence Dictionary', 'id': 'sentencedict', 'url': 'https://sentencedict.com/', 'x-frame-bypass': False},
#     {'name': 'Macmillan Dictionary', 'id': 'macmillan', 'url': 'https://www.macmillandictionary.com/search/british/direct/?q={{ word }}', 'x-frame-bypass': True}
# ]

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":

        word = request.form["word"].lower()
        listDictionaries = request.form.getlist("dictionaries")

        return redirect(url_for("search", word=word))
        
    return render_template("index.html")
    

@app.route('/<word>')
def search(word):

    return render_template("index.html", word=word)