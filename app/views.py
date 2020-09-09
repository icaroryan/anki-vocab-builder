from app import app

from flask import request, render_template, flash, redirect, url_for, session
# from datetime import timedelta

# from urllib.parse import unquote
# import re

app.secret_key = "40e101c7a8b521dffa02b4df"
# app.permanent_session_lifetime = timedelta(days=5)


dictionaries = {
    "cambridge" : {'name': 'Cambridge Dictionary', 'url': 'https://dictionary.cambridge.org/us/search/direct/?datasetsearch=english&q=word_x', 'x-frame-bypass': False},
    "longman" : {'name': 'Longman Dictionary', 'url': 'https://www.ldoceonline.com/search/english/direct/?datasetsearch=english&q=word_x', 'x-frame-bypass': True},
    "thesaurus" : {'name': 'Thesaurus Synonyms', 'url': 'https://www.thesaurus.com/browse/word_x', 'x-frame-bypass': False},
    "gimages" : {'name': 'Google Images', 'url': 'https://cse.google.com/cse?cx=94c82ce85a6c9fa3a#gsc.tab=1', 'x-frame-bypass': True, 'onload': 'google_search_engine'},
    "sentencedict" : {'name': 'Sentence Dictionary', 'url': 'https://sentencedict.com/word_x.html', 'x-frame-bypass': False},
    "macmillan" : {'name': 'Macmillan Dictionary', 'url': 'https://www.macmillandictionary.com/search/british/direct/?q=word_x', 'x-frame-bypass': True},
    "gtranslate" : {'name': 'Google Translate', 'url': 'https://translate.google.com/#view=home&op=translate&sl=en&tl=pt&text=word_x', 'x-frame-bypass': True, 'translator': True},
    "deelp" : {'name': 'DeepL Translate', 'url': 'https://www.deepl.com/translator#en/pt/word_x', 'x-frame-bypass': True, 'translator': True},
    "reverso" : {'name': 'Reverso Context', 'url': 'https://context.reverso.net/translation/english-portuguese/word_x', 'x-frame-bypass': False},
    "michaelis" : {'name': 'Michaelis', 'url': 'https://michaelis.uol.com.br/moderno-ingles/busca/ingles-portugues-moderno/word_x', 'x-frame-bypass': True}
    
}

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        word = request.form["q"].lower()

        dicts = request.form.getlist("d")

        if dicts:
            session["dicts"] = dicts

        return redirect(url_for("query", word=word))
    else:
        return render_template("index.html", dictionaries=dictionaries)
    

@app.route('/<word>')
def query(word):
    if "dicts" in session:
        dicts = session["dicts"]

        return render_template("index.html", word=word, dicts=dicts, dictionaries=dictionaries)
    else:
        return redirect(url_for("index"))