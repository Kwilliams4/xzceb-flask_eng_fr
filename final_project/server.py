from flask import Flask, render_template, request
from machinetranslation import translator
import json


app = Flask(__name__)

#Recibe el texto o input, lo pasa como parametro a la funcion en translator.py. Y retorna el texto traducido.
@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text

#Recibe el texto o input, lo pasa como parametro a la funcion en translator.py. Y retorna el texto traducido.
@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)