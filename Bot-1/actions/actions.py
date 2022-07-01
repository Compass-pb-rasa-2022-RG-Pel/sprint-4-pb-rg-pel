##imports
import os
import nltk
from typing import Any, Text, Dict, List
from newspaper import Article
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

## Baixando dependências NLTK

nltk.data.path.append("/root/nltk_data/")
nltk.download('punkt')

## Aqui está Trazendo variáveis de ambiente para API e MONGODB

MONGO_CLIENT = os.getenv('MONGODB')
API_KEY= os.getenv('API_KEY')

## aqui está a construção das endpoints
CATEGORIES = {
    "esportes":"sports", 
    "geral":"general",
    "ciência":"science",
    "tecnologia":"technology",
    "negócios":"business"
}

ENDPOINTS = {
    'category':"http://api.mediastack.com/v1/news?access_key=ca89b084ffffaa5e905c7c0eda443631&languages=pt&categories=",
    'keyword':"http://api.mediastack.com/v1/news?access_key=ca89b084ffffaa5e905c7c0eda443631&languages=pt&keywords="
}

## Aqui é a função da URL unindo o endpoint da API com o retorno do usuário

def create_path(base,query):
    return base + query

## Função para resumir notícias com NLP

async def get_data(news):
    article = Article(news['url'])
    article.download()
    article.parse()
    article.nlp()
    return article.summary

## Função para solicitar a requisição a API e enviar dados para cliente

async def dispatch_data(dispatcher:CollectingDispatcher,full_path):
    results = requests.get(full_path).json()
    for j in results['data']:
        dispatcher.utter_message(text=j['url'])

    if len(results['data'])>=5:
        for i in range(0,5):
            news = results['data'][i]
            text_sum = await get_data(news)
            
            
            dispatcher.utter_message(text=text_sum)
    else:
        for news in results['data']:
            text_sum = await get_data(news['url'])
            
            dispatcher.utter_message(text=text_sum)

 ## Aqui função Action para retornar os favoritos do usuário

class ActionRemember(Action):


    def name(self) -> Text:
        return "action_remember"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        name = tracker.get_slot("name")




        return []

##Aqui a função Action para requisitar a busca à API e enviar para usuário
class ActionMediaStack(Action):


    def name(self) -> Text:
        return "action_media_stack"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        keyword = tracker.get_slot("keyword")
        name=tracker.get_slot("name")
    

        if keyword in CATEGORIES:
            full_path = create_path(ENDPOINTS['category'],CATEGORIES[keyword])        
            await dispatch_data(dispatcher,full_path)

        else:
            full_path = create_path(ENDPOINTS['keyword'],keyword)            
            await dispatch_data(dispatcher,full_path)

        return []
