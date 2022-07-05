from typing import Any, Text, Dict, List
import requests
import json
import os
import pymongo
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from datetime import datetime
from rasa_sdk.events import SlotSet
from dotenv import load_dotenv
load_dotenv()


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

        slot_id = tracker.get_slot("slot_id")
        slot_lang = tracker.get_slot("slot_lang")
        slot_name = tracker.get_slot("slot_name")
        
        print(slot_lang, slot_id, slot_name)
        
        if(slot_lang == None):
            slot_lang = 'pt'
        if(slot_name == None):
            slot_name = 'user'
        if(slot_id == None):
            slot_id = 0

        db = os.getenv('DB')
        #client = os.getenv('CLIENT_DEVELOP')
        client = os.getenv('CLIENT_PRODUCT')
        collection = os.getenv('COLLECTION')

        json_result = {}
        
        

        
        myclient = pymongo.MongoClient("mongodb://root:root@mongodb:27017")
        mydb = myclient["sprint4"]
        mycon = mydb["rasa"]
        
        print(mycon)
        
        #myclient = pymongo.MongoClient(client)
        #mydb = myclient[db]
        #mycon = mydb[collection]
        
        advices_len = 0
        error = ""

        #try:
        result = mycon.find({"slot_name": slot_name, "slot_id": slot_id, "slot_lang": slot_lang})
        
        for i in result:
            json_result = i
        print('success', len(json_result))
        advices_len = len(json_result)
        #except:
        #    error = 'erro ao buscar o modelo do mongo.'
        if(advices_len == 0):
            try:
                reqAdvice = {}

                if(slot_id == None or slot_id == 0):
                    reqAdvice = requests.get(
                        'https://api.adviceslip.com/advice')
                else:
                    reqAdvice = requests.get(
                        'https://api.adviceslip.com/advice/' + slot_id)

                result = reqAdvice.json()

                url = "https://libretranslate.de/translate"

                payload = json.dumps({
                    "q": result['slip']['advice'],
                    "source": "en",
                    "target": slot_lang,
                    "format": "text",
                })
                headers = {
                  'Content-Type': 'application/json'
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                print(result['slip']['advice'])
                #print(response.json())
                
                advice_translated = response.json()
                                
                output_string = f' - {advice_translated["translatedText"]}'
                #output_string = result['slip']['advice']

                advice = output_string
                mydict = {"slot_name": slot_name, "slot_id": slot_id, "slot_lang": slot_lang, "advice": advice}

                output_string = output_string
                result = mycon.insert_one(mydict)

            except:
               error = 'error em algum lugar da api'
        else:
            output_string = '(Você já recebeu este conselho) ' + json_result['advice']
            
        db = os.getenv('DB')
        #client = os.getenv('CLIENT_DEVELOP')
        client = os.getenv('CLIENT_PRODUCT')
        collection = os.getenv('COLLECTION')
        
        print(db, client, collection)

        dispatcher.utter_message(text=output_string + error)

        return [SlotSet("slot_id", None)]
