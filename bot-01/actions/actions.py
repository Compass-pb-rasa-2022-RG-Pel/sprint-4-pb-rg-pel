# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import re

class ActionProcuraCep(Action):

    def name(self) -> Text:
       return "action_mostra_cep"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        api_adress = 'https://viacep.com.br/ws/'
        cep = tracker.get_slot("cep")
        nome = tracker.get_slot("nome")

##Estruturando a Url para pesquisa
        if re.match(r"[0-9]{8}", cep):
            url = api_adress + cep + '/json'
            json = requests.get(url).json()

            try:
                endereco = "\n"
                endereco += 'CEP: ' + json['cep'] + "\n"
                endereco += 'Logradouro: ' + json['logradouro'] + "\n"
                endereco += 'Complemento: ' + json['complemento'] + "\n"
                endereco += 'Bairro: ' + json['bairro'] + "\n"
                endereco += 'Localidade: ' + json['localidade'] + "\n"
                endereco += 'UF: ' + json['uf'] + "\n"
                endereco += 'IBGE: ' + json['ibge'] + "\n"
                endereco += 'GIA: ' + json['gia'] + "\n"
                endereco += 'DDD: ' + json['ddd'] + "\n"
                endereco += 'SIAFI: ' + json['siafi'] + "\n"

                dispatcher.utter_message(text=f"Obrigado {nome} por me utilizar, seguem os dados do CEP inserido {cep}.\n{endereco}")

            except:
                dispatcher.utter_message(text=f"Seguinte {nome}, o CEP {cep} não contém nenhum registro na base de dados, verifique certinho e tente novamente a pesquisa!")

            finally:
                return [SlotSet("cep", None)]

        else:
            dispatcher.utter_message(text=f"Seguinte {nome}, o CEP {cep} informado é inválido, verifique certinho e tente novamente!")
            return [SlotSet("cep", None)]