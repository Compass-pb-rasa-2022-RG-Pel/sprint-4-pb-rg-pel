
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
import os
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


        #Conexão com o MongoDB 
        client = MongoClient(f"mongodb+srv://bancodog:FgKM0S4I4uoni4Nd@apidog.kx9ryjo.mongodb.net/?retryWrites=true&w=majority")
        db = client["api-dog"]
        collection = db["collection-dog"]
        print(db)

        dog = tracker.get_slot("breeds") 
        url= f'https://dog.ceo/api/breed/{dog}/images/random' 
        usuario = tracker.get_slot("usuario")
        print(dog, usuario)

        try: 
            contador = collection.count_documents({"usuario": usuario, "dog": dog})
            print(contador)
            if int(contador) >0:
                print("entrou no if")
                dispatcher.utter_message(text = "você já pesquisou sobre esse cachorro")
                doguinho = collection.find_one({"usuario": usuario, "dog": dog})
                data_db = doguinho.get("url")
                resposta = f'{usuario}, o cachorro solicitado é da raça {dog} e pode ser visto no link {data_db} <image src={data_db} height=100px ></image>'
                dispatcher.utter_message(text = resposta)

            else: 
                print("entrou no else")
                retorno = requests.get(url).json()
                link = retorno.get('message')  
                resposta = f"{usuario}, o cachorro solicitado é da raça {dog} e pode ser visto no link {link} <image src={link} height=100px ></image>"

                dispatcher.utter_message(text= resposta)

                documento = {
                    "usuario": usuario,
                    "dog": dog,
                    "url": link,
                }
                collection.insert_one(documento)
        except: 
            print("erro no try")

        return [SlotSet("breeds", url)]

        