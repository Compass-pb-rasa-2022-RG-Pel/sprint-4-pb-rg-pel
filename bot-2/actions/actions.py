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

# function to conect with mongo


def ConectMongo():
    try:
        # client = MongoClient(
        #     'mongodb://localhost:27017/?directConnection=true')
        client = MongoClient(f'mongodb+srv://{DB_NAME}:{DB_PASS}@weatherdb.cm3rmpi.mongodb.net/?retryWrites=true&w=majority')
        db = client.weather_bot
        collection = db.data_search
        collection.insert_one({"user": "name", "searched_city": "city"})

    except:
        print("deu ruim com o banco")

    return db, collection

# function to verify if the city is already consulted


def AlreadyConsulted(name, city, collection):
    try:
        if int(collection.count_documents({"user": name, "searched_city": city})) > 0:
            return True
        else:
            return False
    except:
        print("deu ruim na consulta")

# function to request data to Weather API


def RequestAPI(city):
    try:
        base_request = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        res = requests.get(base_request)
        return res.json()
    except:
        print("deu ruim na RequestAPI")

# main function of rasa actions


class ActionSearchCity(Action):

    def name(self) -> Text:
        return "action_search_city"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Connect with mongoDB
        db, collection = ConectMongo()
        # Getting user data from slots
        user_name = tracker.get_slot('name').title()
        city = tracker.get_slot('city').title()

        # Checking if the consulting is already done
        if AlreadyConsulted(user_name, city, collection):
            post = collection.find_one({"user": user_name, "searched_city": city})
            # informing to user that it already searched by the solicited city
            dispatcher.utter_message(
                text=f"{user_name}, você já pesquisou sobre a temperatura nessa cidade:")
            # get data variables from database
            city_db = post.get("searched_city")
            temp_db = post.get("temp")
            # informing the user the temperature in requested city from database
            dispatcher.utter_message(
                text=f"A temperatura em {city_db} é {temp_db}°C")

        else:
            # call the API function to get data
            res = RequestAPI(city)
            # set temperature data from API
            temperature = res.get('main').get('temp')
            # inform to user the temperature in requested city
            dispatcher.utter_message(
                text=f"A temperatura em {city} é {temperature}°C")
            # Defining post object
            post = {
                "user": user_name,
                "searched_city": city,
                "temp": temperature
            }
            # insert post to database
            collection.insert_one(post)

        return []
