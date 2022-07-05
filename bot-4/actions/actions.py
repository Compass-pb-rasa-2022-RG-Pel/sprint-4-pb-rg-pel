# imports

from readline import insert_text
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
import os
from pymongo import MongoClient




class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "cat_form"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        user = tracker.get_slot('user')
        cat = tracker.get_slot("breeds")

       
       
        DB_USER = "rasa-rasa"
        DB_PASS = "rasaapicat"
      

        # conexão com o MongoDB
        client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASS}@clustercat.5ztbxvd.mongodb.net/?retryWrites=true&w=majority")
        db = client["rasa-api"]
        collection = db["cats-collection"]
        print(db)

    
        

        if (collection.count_documents({"cat":cat})):
            
            consulta = collection.find_one({"cat":cat})
            catDB = consulta.get("cat")
            imgDB = consulta.get("imgURL")
            dispatcher.utter_message(text= f"O gato {catDB} já foi consultado. Abaixo o resultado da pesquisa")
            dispatcher.utter_message(image = imgDB)

        else:

            url= f'https://api.thecatapi.com/v1/images/search?breeds_ids={cat}'
            json_data = requests.get(url).json()
            imgURL = json_data[0].get('url')
            
            resp = f"Olá {user}, o você solicitou o gato raça {cat}, aqui estão link {imgURL}"

            post = {
                "user": user,
                "cat": cat,
                "imgURL":imgURL
                }

            collection.insert_one(post)

            dispatcher.utter_message(text= resp)
            dispatcher.utter_message(image= imgURL)

            return [SlotSet("breeds", url)]

## img: data[0].url, cat_type, name: data[0].breeds[0].name

    