# Avaliação Sprint 4 - Programa de Bolsas Compass.uol e universidades de Rio Grande e Pelotas
Avaliação da quarta sprint do programa de bolsas Compass.uol para formação em chatbot Rasa.

---
# Chatbot - Dog API

O chatbot construído tem como objetivo criar uma conversa com o usuário a qual ele irá armazenar o nome do usuário e após este informar sua inteção em ver um cachorro e sua respectiva raça, o bot retornará uma mensagem e um link com a imagem, bem como a imagem.


## Desenvolvimento

Dependências

Python 3.8.13

Rasa

MongoDB

Docker e docker-compose

Okteto

Conexão com a API

A API utilizada nesse projeto foi a DOG API  https://dog.ceo/api/breed/{dog}/images/random, a qual, a partir da escrita da raça do cachorro busca a respectiva imagem.

![image](https://user-images.githubusercontent.com/71715202/177291249-62ae6c24-744e-48cd-b9ff-29b363a05db9.png)


# Utilizando o ChatBot


Para utilizar a aplicação com o bot, basta abrir um terminal e executar o comando "run rasa actions", e em outro terminal executar o comando "rasa shell" e então é só iniciar uma conversa com o bot.

Dê os cumprimentos ao chatbot

Diga sua intenção ao chatbot

Digite o seu primeiro nome

Informe a raça do cachorro que deseja visualizar

---

# Features
 
 Usuário informa seu nome

 Usuário solicita saber sobre uma raça de cachorro

 Salvar histórico de pesquisa do usuário

 Retornar a solicitação/ histórico de pesquisa de um usuário caso tenha se repetido(preferência)

Setup

Inicializando ambiente virtual com:

source ../venv/bin/activate

python=3.8.13


Bot-1
<<<<<<< HEAD

Tecnologias usadas:

Rasa
Node.js

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


Bot-2


Rasa

Node.js

MongoDB

Instalar dependências

pip install -r requirements.txt

Treinando bot

rasa train

Executando o bot shell

rasa run --cors "*"

start rasa server

rasa run actions

acessar localmente com o arquivo index.html (Abra o arquivo em um navegador qualquer)

Foi conectado ao mongoDB

Dificuldade encontrada: configurar o dotenv adquadamente.

Bot-3


Testando com docker

Executar

docker-compose up

acessar localmente com o arquivo index.html (Abra o arquivo em um navegador qualquer)

Foram desenvolvidos containers, um para as actions, outro para o rasa, e outro para o banco MongoDB. Foi criado também o arquivo docker-compose.yml (para a execução ordenada dos arquivos dockerfile)

Bot-4

Rasa

Node

Docker

Kubernetes - Okteto

Subindo o Bot-4 no okteto pelo CLI

comando:

okteto deploy --build   -->

![image](https://user-images.githubusercontent.com/71715202/177292513-f73862ab-52f3-4ff0-8e05-7fe1617726c6.png)

![image](https://user-images.githubusercontent.com/71715202/177291715-e81c3421-5be7-494b-b186-9edac7850c2f.png)

link para visualização do bot no Okteto:

https://web-tatius7.cloud.okteto.net/
--- -->
