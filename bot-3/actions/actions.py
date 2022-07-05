# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Collection, Text, Dict, List

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
        # print(earth_date)

        #corrigindo formato da data para acessar a api

        array = earth_date.split("/")
        new_date = array[2] + "-" + array[1] + "-" + array[0]
        print(new_date)

        # conexão com o MongoDB via atlas

        client = MongoClient(f"mongodb+srv://usuariox:GTuJf2pOvuHNPRzc@cluster0.cbrwelh.mongodb.net/?retryWrites=true&w=majority")
        db = client["mars-api"]
        collection = db["collection-mars"] 

        # print(db) #ver no terminal se esta retornando do banco

        api_url= f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key=DEMO_KEY&earth_date={new_date}' 

        json_data = requests.get(api_url).json()
        photo = json_data.get('photos') 
        # print(api_url, photo[0]["img_src"])
        #variavel para receber o endereço da foto no JSON da API
        url = photo[0]["img_src"]
        
        try:
            cont = collection.count_documents({"usuario": usuario, "new_date": new_date})
            print(cont)
            if int(cont) >0:
                print("entrou no if")
                dispatcher.utter_message(text = "você já pesquisou a foto dessa data")
                photo_banco = collection.find_one({"usuario": usuario, "new_date": new_date})
                data_db = photo_banco.get("url")    
                #usa variavel earth_date na resposta para mostrar a data na formatacao do usuario
                resposta = f"{usuario}, a foto de marte nessa data {earth_date} é..."

                dispatcher.utter_message(text= resposta)
                dispatcher.utter_message(image= url)
            else: 
                print("entrou no else")
                retorno = requests.get(api_url).json()
                new_photo = retorno.get('photos')
                link = new_photo[0]['img_src']
                resposta = f"{usuario}, aqui está uma foto de marte na data: {earth_date}  "

                dispatcher.utter_message(text =resposta)
                dispatcher.utter_message(image= link)

                documento = {
                    "usuario": usuario,
                    "new_date": new_date,
                    "url": link,
                }
                collection.insert_one(documento)

        except:
            print("erro no try")
        return [SlotSet("earth_date", api_url)]


        # return[]
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
        