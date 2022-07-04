
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
import os
# from dotenv import load_dotenv
from pymongo import MongoClient
from readline import insert_text

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "dog_form"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        usuario = tracker.get_slot('usuario')
        dog = tracker.get_slot("breeds")

        ## Lendo arquivo .env
        # dotenv_path = os.path.join(os.path.dirname(__file__), '/.env') 
        # print(dotenv_path)      
        # load_dotenv(dotenv_path)
        # DB_USER = "tatieli"
        # DB_PASS = "rasa123"
        # print(DB_USER)
        # print(DB_PASS)

         # conexão com o MongoDB
        client = MongoClient(f"mongodb+srv://bancodog:FgKM0S4I4uoni4Nd@apidog.kx9ryjo.mongodb.net/?retryWrites=true&w=majority")
        db = client["api-dog"]
        collection = db["collection-dog"]
        print(db)

    
        url= f'https://dog.ceo/api/breed/{dog}/images/random'
        json_data = requests.get(url).json()
        data = json_data.get('message')

        if (collection.count_documents({"dog":dog})):

            resp = "Esse cachorro já consta na nossa consulta"
            dispatcher.utter_message(text= resp)
            
            consulta = collection.find_one({"dog":dog})
            dogDB = consulta.get("dog")
            resp2 = f"Voce pode ver aqui {dogDB}"
            dispatcher.utter_message(text= resp2)


        else:
            
            resp = f"Olá {usuario}, o você solicitou o cachorro da raça {dog}, aqui estão link {data} <image src={data} height=100px ></image>"

            res = {"usuario": usuario, "dog": dog, "url":url}

            collection.insert_one(res)

            dispatcher.utter_message(text= resp)

            return [SlotSet("breeds", url)]
