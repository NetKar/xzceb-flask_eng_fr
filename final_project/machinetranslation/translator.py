'''
To Translate
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
'''
apikey = os.environ['6iGJ1ZtElyIn8v_7LTCKE52-Rxkl8PrxRJThQFtGbS0F']
url = os.environ['https://api.jp-tok.language-translator.watson.' +
'cloud.ibm.com/instances/8cdb976a-a930-4b45-a634-60110a379304']
'''
AUTHENTICATOR = IAMAuthenticator('6iGJ1ZtElyIn8v_7LTCKE52-Rxkl8PrxRJThQFtGbS0F')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)
language_translator.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/8cdb976a-a930-4b45-a634-60110a379304')

def english_to_french(english_text):
    '''To translate Eng to Fr'''
    french_text = language_translator.translate(
    text=english_text,
    model_id="en-fr").get_result()
    phrase = list(french_text.values())[0]
    trans = phrase[0]
    tv= list(trans.values())[0]
    return tv

def french_to_english(french_text):
    '''To translate Fr to Eng'''
    english_text = language_translator.translate(
    text=french_text,
    model_id="fr-en").get_result()
    phrase = list(english_text.values())[0]
    trans = phrase[0]
    tv= list(trans.values())[0]
    return tv
