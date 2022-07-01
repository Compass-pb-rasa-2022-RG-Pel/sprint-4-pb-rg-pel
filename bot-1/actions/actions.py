# imports

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "cat_form"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        cat = tracker.get_slot("breeds") 
        url= f'https://api.thecatapi.com/v1/images/search?breeds_ids={cat}'
        user = tracker.get_slot('user')

        json_data = requests.get(url).json()
        data = json_data[0].get('url')
        print(data)
        resp = f"Olá {user}, o você solicitou o gato raça {cat}, aqui estáo link {data} <image src={data} height=100px ></image>"
      

        dispatcher.utter_message(text= resp)

        return [SlotSet("breeds", url)]


## img: data[0].url, cat_type, name: data[0].breeds[0].name