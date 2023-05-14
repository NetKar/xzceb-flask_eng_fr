from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    '''To translate Eng to Fr'''
    french_text = language_translator.translate(
    text=textToTranslate,
    model_id="en-fr").get_result()
    phrase = list(french_text.values())[0]
    trans = phrase[0]
    tv= list(trans.values())[0]
    print(tv)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    '''To translate Fr to Eng'''
    english_text = language_translator.translate(
    text=textToTranslate,
    model_id="fr-en").get_result()
    phrase = list(english_text.values())[0]
    trans = phrase[0]
    tv= list(trans.values())[0]
    print(tv)
    return "Translated text to English"

@app.route("/")
def renderIndexPage(res):
    res.render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
