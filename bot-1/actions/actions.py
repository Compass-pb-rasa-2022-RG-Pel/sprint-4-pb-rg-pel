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
import os
from pymongo import MongoClient

class ActionMarsForms(Action):

    def name(self) -> Text:
        return "action_mars_form"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        usuario = tracker.get_slot("usuario")
        earth_date = tracker.get_slot("earth_date")
        print(earth_date)

        #corrigindo formato da data para acessar a api

        array = earth_date.split("/")
        new_date = array[2] + "-" + array[1] + "-" + array[0]
        print(new_date)

        # try:

        api_url= f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key=DEMO_KEY&earth_date={new_date}' 

        json_data = requests.get(api_url).json()
        photo = json_data.get('photos') 
        print(api_url, photo[0]["img_src"])
        url = photo[0]["img_src"]
        # return[]
        resposta = f"{usuario}, a foto de marte da data {earth_date} é <image src={url} height=100px ></image>"

        dispatcher.utter_message(text= resposta)

        return [SlotSet("earth_date", api_url)]


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# class ActionUserForms(Action):

#     def name(self) -> Text:
#         return "action_user_form"
    
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         usuario = tracker.get_slot('usuario')
        