"""
FGM: Code for translate from english to french, with ibm_watson
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
   version='2018-05-01',
   authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function return translation english to french
    """
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    ##print(json.dumps(french_text, indent=2, ensure_ascii=False))
    ###print(french_text)

    json_object = json.loads(json.dumps(french_text, indent=2, ensure_ascii=False))

    return json_object["translations"][0]["translation"]

def french_to_english(french_text):
    """
    This function return translation french to english.
    """
    #write the code here
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    ##french_translation = json.dumps(english_text, indent=2, ensure_ascii=False)
    
    ###print(english_text)
    json_object = json.loads(json.dumps(english_text, indent=2, ensure_ascii=False))
    ###print(json_object["translations"][0]["translation"])
    ###print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return json_object["translations"][0]["translation"]
