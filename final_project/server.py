from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

AUTHENTICATOR = IAMAuthenticator('6iGJ1ZtElyIn8v_7LTCKE52-Rxkl8PrxRJThQFtGbS0F')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)
language_translator.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/8cdb976a-a930-4b45-a634-60110a379304')

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
    print("Translated text to French")
    return tv

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
    print("Translated text to English")
    return tv

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
