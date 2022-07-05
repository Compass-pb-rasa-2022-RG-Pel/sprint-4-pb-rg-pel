import datetime as dt 
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from pymongo import MongoClient

class Habilidades(Action):    
    def name(self) -> Text:
        return "action_exiba_habilidades"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        pokemon = tracker.slots['nome_pokemon'].lower()        
        data_atual = dt.datetime.now().date()
        id_conexao = tracker.sender_id
        usuario = tracker.slots['usuario']
        
        print (f'ID: {id_conexao}')
        print (f'Dia: {data_atual}')
        print (f'Nome: {usuario}')
        print (f'Pokemon: {pokemon}')
        
        try:
            client = MongoClient("mongodb://root:root@mongodb:27017/")
            database = client["sprint4"]
            minha_colecao = database["pokemons"]
            
            #if int(minha_colecao.count_documents({"usuario": usuario, "pokemon": pokemon})) > 0:
            #    dispatcher.utter_message(text=f"Você já consultou o pokemon {pokemon}")
            #else:
            #    print("Não localizado")
                
        except:
            print("Não foi possível conectar ao banco de dados")
                    
        try:
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

            objeto_pokemon = requests.get(url).json()
            nome = (objeto_pokemon['forms'][0]['name'])
            vida = (objeto_pokemon['stats'][0]['base_stat'])
            ataque = (objeto_pokemon['stats'][1]['base_stat'])
            defesa = (objeto_pokemon['stats'][2]['base_stat'])
            ataque_especial = (objeto_pokemon['stats'][3]['base_stat'])
            defesa_especial = (objeto_pokemon['stats'][4]['base_stat'])
            velocidade = (objeto_pokemon['stats'][5]['base_stat'])
            link_foto = (objeto_pokemon['sprites']['other']['home']['front_default'])
            
        except:
            dispatcher.utter_message(text=f'Não foi possível localizar este pokemon, verifique se {pokemon} é o nome de um pokemon')
            return[]


        if tracker.slots['usuario'] == None:
            dispatcher.utter_message(text=f"Antes de continuar, digite seu nome. Pode começar com: 'Meu nome é ...'")
            return [] 
        else:
            dispatcher.utter_message(text=f"NOME: {nome}")
            dispatcher.utter_message(text=f"VIDA: {vida}")
            dispatcher.utter_message(text=f"ATAQUE: {ataque}")
            dispatcher.utter_message(text=f"DEFESA: {defesa}")
            dispatcher.utter_message(text=f"ATAQUE ESPECIAL: {ataque_especial}")
            dispatcher.utter_message(text=f"DEFESA ESPECIAL: {defesa_especial}")
            dispatcher.utter_message(text=f"VELOCIDADE: {velocidade}")
            dispatcher.utter_message(image = link_foto)
            
            registro = [{"usuario": usuario, "pokemon": nome, "vida": vida, "ataque": ataque, "defesa": defesa, "ataque especial": ataque_especial, "defesa especial": defesa_especial, "velocidade": velocidade, "imagem": link_foto, "data atual": data_atual, "id da conexão": id_conexao}]
            
            minha_colecao.insert_many(registro)
            
            return [SlotSet("nome_pokemon", None)] 