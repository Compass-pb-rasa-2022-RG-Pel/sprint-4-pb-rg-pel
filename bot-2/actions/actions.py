# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import requests
import os
from dotenv import load_dotenv
from pymongo import MongoClient

class ActionFilms(Action):

    def name(self) -> Text:
         return "action_show_films"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["name"]
        name = tracker.get_slot("name")
        print("1")
        # Acessa a API para mostrar todos os filmes
        api_url = "https://swapi.dev/api/films/"

        json_data = requests.get(api_url).json()
        print("2")
        try:    
            dispatcher.utter_message(text=f"{name}, aqui estão todos os filmes da franquia original: ")
            ct=0
            while(ct < 6):
                # Mostra na tela, os resultados dos títulos dos filmes, colhidos da API
                titulo = json_data['results'][ct]['title']
                episodio = json_data['results'][ct]['episode_id']
                dispatcher.utter_message(text=f"Episodio: {episodio} - {titulo}\n ")
                ct = ct+1
        except: 
            titulo = json_data['error']
            dispatcher.utter_message(text=f"Opa {name}, não localizamos sua solicitação!")
        finally:
            # Não deixa enviar o nome vazio!
            for slot_name in required_slots:
                if tracker.slots.get(slot_name) is None:
                    # The slot is not filled yet. Request the user to fill this slot next.
                    return [SlotSet("requested_slot", slot_name)]

class ActionFilmsInform(Action):

    def name(self) -> Text:
         return "action_show_inform"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["film_name"]
        film_name = tracker.get_slot("film_name")

        ## Lendo arquivo .env
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')       
        load_dotenv(dotenv_path)

        DB_USER = os.getenv("DB_USER")
        DB_PASS = os.getenv("DB_PASS")

        #Conexão com o MongoDB
        client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASS}@apicluster.zyhrttc.mongodb.net/?retryWrites=true&w=majority")
        db = client["database"]
        collection = db["filmes"]
    
        if int(film_name) > 6 or int(film_name) < 1:
            dispatcher.utter_message(text=f"Opa, não localizamos sua solicitação!")
        else:
            # Acessa a API para mostrar todos os filmes
            api_url = "https://swapi.dev/api/films/"

            json_data = requests.get(api_url).json()
            try:    
                dispatcher.utter_message(text=f"Essas são as informações sobre o episódio {film_name}: ")
                ct=0
                while(ct < 6):
                    episodio = json_data['results'][ct]['episode_id']
                    if episodio == int(film_name):
                        print("entrei")
                        titulo = json_data['results'][ct]['title']
                        resumo = json_data['results'][ct]['opening_crawl']
                        diretor = json_data['results'][ct]['director']
                        produtor = json_data['results'][ct]['producer']
                        data_lan = json_data['results'][ct]['release_date']
                        #Inserindo dados no mongo DB
                        insertSearch = {'title': titulo,'release_date': data_lan}
                        collection.insert_one(insertSearch)
                        # Mostra na tela, os resultados dos títulos dos filmes, colhidos da API
                        dispatcher.utter_message(text=f"Título Original: {titulo} \n Diretor: {diretor} \n Produtores: {produtor} \n Data de Lançamento: {data_lan} \n Resumo: \n {resumo}")
                    ct = ct+1
            except: 
                titulo = json_data['error']
                dispatcher.utter_message(text=f"Opa, não localizamos sua solicitação!")
            finally:
                # Não deixa enviar o nome vazio!
                for slot_name in required_slots:
                    if tracker.slots.get(slot_name) is None:
                        # The slot is not filled yet. Request the user to fill this slot next.
                        return [SlotSet("requested_slot", slot_name)]

