# imports

from readline import insert_text
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
import os
from dotenv import load_dotenv
from pymongo import MongoClient



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "cat_form"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        user = tracker.get_slot('user')
        cat = tracker.get_slot("breeds")

        ## Lendo arquivo .env
        dotenv_path = os.path.join(os.path.dirname(__file__), '../bot-2/.env')       
        load_dotenv(dotenv_path)
        DB_USER = "rasa-rasa"
        DB_PASS = "rasaapicat"
        print(DB_USER)
        print(DB_PASS)

         # conexão com o MongoDB
        client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASS}@clustercat.5ztbxvd.mongodb.net/?retryWrites=true&w=majority")
        db = client["rasa-api"]
        collection = db["cats-collection"]
        print(db)

    
        url= f'https://api.thecatapi.com/v1/images/search?breeds_ids={cat}'
        json_data = requests.get(url).json()
        data = json_data[0].get('url')

        if (collection.count_documents({"cat":cat, "url":url})):

            resp = "Esse gato já consta na nossa consulta"
            dispatcher.utter_message(text= resp)
            
            consulta = collection.find({"cat":cat, "url":url})
            catDB = consulta.get("cat", "url")
            resp2 = f"Voce pode conferir aqui {catDB}"
            dispatcher.utter_message(text= resp2)


        else:
            
            resp = f"Olá {user}, o você solicitou o gato raça {cat}, aqui estão link {data} <image src={data} height=100px ></image>"

            res = {"user": user, "cat": cat, "url":url}

            collection.insert_one(res)

            dispatcher.utter_message(text= resp)

            return [SlotSet("breeds", url)]

         



## img: data[0].url, cat_type, name: data[0].breeds[0].name

    