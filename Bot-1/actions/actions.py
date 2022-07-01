# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
# import os
# from dotenv import load_dotenv
# from pymongo import MongoClient


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "dog_form"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        dog = tracker.get_slot("breeds") 
        url= f'https://dog.ceo/api/breed/{dog}/images/random' 
        usuario = tracker.get_slot('usuario')

        json_data = requests.get(url).json()
        # print(type(json_data))
        data = json_data.get('message') 
        print(data)
        resposta = f"{usuario}, o cachorro solicitado é da raça {dog} e pode ser visto no link {data} <image src={data} height=100px ></image>"
      

        dispatcher.utter_message(text= resposta)

        return [SlotSet("breeds", url)]
        # return[]
