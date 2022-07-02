# This files contains your custom actions which can be used to run
# custom Python code.
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionSearchCity(Action):

    def name(self) -> Text:
        return "action_search_city"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_name = tracker.get_slot('name')
        city = tracker.get_slot('city').title()
        API_KEY = 'cd94ea11ea101c7443a5613e10993ad0'
        base_request = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

        res = requests.get(base_request)
        json_response = res.json()
        temperature = json_response.get('main').get('temp')

        dispatcher.utter_message(
            text=f"A temperatura em {city} é {temperature}°C")

        return []
