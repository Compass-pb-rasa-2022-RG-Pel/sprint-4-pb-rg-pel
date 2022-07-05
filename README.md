# Avaliação Sprint 4 - Programa de Bolsas Compass.uol e universidades de Rio Grande e Pelotas
Avaliação da quarta sprint do programa de bolsas Compass.uol para formação em chatbot Rasa.

---
# Chatbot - Dog API

O chatbot construído tem como objetivo criar uma conversa com o usuário a qual ele irá armazenar o nome do usuário e após este informar sua inteção em ver um cachorro e sua respectiva raça, o bot retornará uma mensagem e um link com a imagem, bem como a imagem.


## Desenvolvimento

Dependências

Python 3.8

Rasa

Conexão com a API

A API utilizada nesse projeto foi a DOG API  https://dog.ceo/api/breed/{dog}/images/random, a qual, a partir da escrita da raça do cachorro busca a respectiva imagem.

# Utilizando o ChatBot


Para utilizar a aplicação com o bot, basta abrir um terminal e executar o comando "run rasa actions", e em outro terminal executar o comando "rasa shell" e então é só iniciar uma conversa com o bot.

Dê os cumprimentos ao chatbot

Diga sua intenção ao chatbot

Digite o seu primeiro nome

Informe a raça do cachorro que deseja visualizar

---
# Features
 
 Usuário informa seu nome

 Usuário solicita ver uma raça de cachorro

 Salvar histórico de pesquisa do usuário

 Retornar a solicitação/ histórico de pesquisa de um usuário caso tenha se repetido(preferência)

Setup

Inicializando ambiente virtual com:

source ../venv/bin/activate

python=3.8.13

use pipenv

pipenv install


Bot-1
<<<<<<< HEAD

Testando localmente

Instalar dependências

pip install -r requirements.txt

=======

Treinando bot

rasa train

Executando o bot shell

rasa run --cors "*"

start rasa server

rasa run actions

acessar localmente com o arquivo index.html (Abra o arquivo em um navegador qualquer)

http://localhost:5005/webhooks/rest/webhook



Bot-2

Testando MongoDB

Instalar dependências

pip install -r requirements.txt

Treinando bot

rasa train

Executando o bot shell

rasa run --cors "*"

start rasa server

rasa run actions

acessar localmente com o arquivo index.html (Abra o arquivo em um navegador qualquer)
http://localhost:5005/webhooks/rest/webhook

Bot-3


Testando com docker

Executar

 docker-compose up

acessar localmente com o arquivo index.html (Abra o arquivo em um navegador qualquer)
http://localhost:5005/webhooks/rest/webhook

Bot-4

Subindo o chat no okteto pelo CLI

okteto deploy --build   -->

https://web-tatius7.cloud.okteto.net/
--- -->
