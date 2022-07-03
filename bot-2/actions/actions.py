# This files contains your custom actions which can be used to run
# custom Python code.
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Environment variables
config = load_dotenv('../sprint-4-pb-rg-pel/.env')
API_KEY = "cd94ea11ea101c7443a5613e10993ad0"
DB_NAME = "fernando"
DB_PASS = "fSjIiRhEXnwKy8Ch"


def ConectMongo():
    try:
        client = MongoClient(
            f'mongodb+srv://{DB_NAME}:{DB_PASS}@weatherdb.cm3rmpi.mongodb.net/?retryWrites=true&w=majority')
        db = client.historical_search
        collection = db.data_search

    except:
        print("deu ruim com o banco")

    return client, db, collection


def AlreadyConsulted(name, city, collection):
    try:
        if int(collection.count_documents({"user": name, "searched_city": city})) > 0:
            return True
        else:
            return False
    except:
        print("deu ruim na consulta")


def RequestAPI(city):
    try:
        base_request = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        res = requests.get(base_request)
        return res.json()
    except:
        print("deu ruim na RequestAPI")


class ActionSearchCity(Action):

    def name(self) -> Text:
        return "action_search_city"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Connect with mongoDB
        client, db, collection = ConectMongo()
        # Getting user data from slots
        user_name = tracker.get_slot('name').title()
        city = tracker.get_slot('city').title()

        # Checking if the consulting is already done
        if AlreadyConsulted(user_name, city, collection):
            post = collection.find_one({"user": user_name})
            # informing to user that it already searched by the solicited city
            dispatcher.utter_message(
                text=f"{user_name}, você já pesquisou sobre a temperatura nessa cidade:")
            # get data variables from database
            city_db = post.get("searched_city")
            temp_db = post.get("temp")

            dispatcher.utter_message(
                text=f"A temperatura em {city_db} é {temp_db}°C")

        else:
            # call the API function to get data
            res = RequestAPI(city)
            # set temperature data from API
            temperature = res.get('main').get('temp')
            # inform to user the temperature 
            dispatcher.utter_message(
                text=f"A temperatura em {city} é {temperature}°C")
            # Defining post element
            post = {
                "user": user_name,
                "searched_city": city,
                "temp": temperature
            }
            # insert to database the searched info
            collection.insert_one(post)

        return []
