# imports
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
from newspaper import Article
from pymongo import MongoClient
import pymongo
import os
import nltk

# Baixando dependências NLTK
nltk.data.path.append("/root/nltk_data/")
nltk.download('punkt')

# Aqui está Trazendo variáveis de ambiente para API e MONGODB
#MONGO_CLIENT = os.getenv('MONGODB')
API_KEY = os.getenv('API_KEY')


# aqui está a construção de endpoints
CATEGORIES = {
    "esportes": "sports", "geral": "general", "ciência": "science", "tecnologia": "technology",
    "entretenimento": "entertainment", "saúde": "health", "negócios": "business"
}

ENDPOINTS = {
    'category': "http://api.mediastack.com/v1/news?access_key=ca89b084ffffaa5e905c7c0eda443631&languages=pt&categories=",
    'keyword': "http://api.mediastack.com/v1/news?access_key=ca89b084ffffaa5e905c7c0eda443631&languages=pt&keywords="
}


# Aqui é a função da URL unindo o endpoint da API com o retorno do usuário
def create_path(base, query):
    return base + query


# Função para resumir notícias com NLP
async def get_data(news):
    article = Article(news['url'])
    article.download()
    article.parse()
    article.nlp()
    return article.summary

# Função para solicitar a requisição a API e enviar dados para cliente


async def dispatch_data(dispatcher: CollectingDispatcher, full_path):
    results = requests.get(full_path).json()
    noticias = []

    for j in results['data']:
        dispatcher.utter_message(text=j['url'])
        noticias.append(j['url'])

    return noticias


# Aqui a função Action para requisitar busca à API e enviar para usuário
#  e já acessar o mongo e salvar o historico do usuario
class ActionMediaStack(Action):

    def name(self) -> Text:
        return "action_media_stack"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        keyword = tracker.get_slot("keyword")
        name = tracker.get_slot("name")
        client = MongoClient("mongodb://root:root@mongodb:27017/")
        #client = MongoClient("mongodb+srv://Rodrigo:rasa1234@cluster0.9nwjp.mongodb.net/?retryWrites=true&w=majority")
        db = client["rasa"]
        collection = db["history"]

        if keyword in CATEGORIES:
            full_path = create_path(ENDPOINTS['category'], CATEGORIES[keyword])
            noticias = await dispatch_data(dispatcher, full_path)
            collection.insert_one(
                {'name': name, 'keyword': keyword, 'kind': 'category', 'list': noticias})

        else:
            full_path = create_path(ENDPOINTS['keyword'], keyword)
            noticias = await dispatch_data(dispatcher, full_path)
            collection.insert_one(
                {'name': name, 'keyword': keyword, 'kind': 'keyword'})

        return []
