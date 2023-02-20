import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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
    Translates English text to French using the IBM Watson Language Translator service.
    """
    translation_response = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    )
    french_text = translation_response.get_result(
    )['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English using the IBM Watson Language Translator service.
    """
    translation_response = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    )
    english_text = translation_response.get_result()[
        'translations'][0]['translation']
    return english_text
