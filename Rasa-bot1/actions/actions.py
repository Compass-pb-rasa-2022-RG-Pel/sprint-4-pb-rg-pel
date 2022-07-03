from typing import Any, Text, Dict, List
from importlib_metadata import method_cache
import requests
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from datetime import datetime
from rasa_sdk.events import SlotSet

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_horas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        time_now = datetime.now()
        formated_time = time_now.strftime("%H:%M:%S")
        output_string = f'Agora são {formated_time}'

        dispatcher.utter_message(text=output_string)

        return []

class ActionAdviceslip(Action):

    def name(self) -> Text:
        return "action_advice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output_string = ''
        id = tracker.get_slot("slot_id")
        lang = tracker.get_slot("slot_lang")
        print(lang)
        try:
            #
            reqAdvice = {}

            if(id == None):
                reqAdvice = requests.get('https://api.adviceslip.com/advice')
            else:
                reqAdvice = requests.get('https://api.adviceslip.com/advice/'+ id)
                
            result = reqAdvice.json()
            
            body = {
                'q':result['slip']['advice'],
                'source':"en",
                'target':"pt",
                'format':"text",
            }
            #reqTranslate = requests.post('https://lt.vern.cc/translate', json=body)
            #print(result['slip']['advice'])
            #advice = reqTranslate.json()
            #output_string = f' - {advice["translatedText"]}'
            output_string = result['slip']['advice']
        except:
            #
            print('error em algum lugar')

        #time_now = datetime.now()
        #formated_time = time_now.strftime("%H:%M:%S")

        dispatcher.utter_message(text=output_string)

        return [SlotSet("slot_id", None)]

