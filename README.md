# Avaliação Sprint 4 - Programa de Bolsas Compass.uol e universidades de Rio Grande e Pelotas
Avaliação da quarta sprint do programa de bolsas Compass.uol para formação em chatbot Rasa.

---

## Execução

- Bot-1: **Crie um bot Rasa em Português** que use um formulário para pegar o nome e uma preferência do usuário para acessar a API utilizada nas [sprint 1](https://github.com/Compass-pb-rasa-2022-RG-Pel/sprint-1-pb-rg-pel) e/ou [sprint 2](https://github.com/Compass-pb-rasa-2022-RG-Pel/sprint-2-pb-rg-pel). O bot questiona o usuário, cujas respostas irão para slots em um form. A consulta à API deverá ocorrer em uma action e retornar o dado em texto e/ou imagem ao usuário. Dicas de forms: <https://learning.rasa.com/rasa-forms-3/> e código em <https://github.com/RasaHQ/rasa-3.x-form-examples>
- Bot-2: Agregue o banco de dados ao bot-1, como feito na [sprint 2](https://github.com/Compass-pb-rasa-2022-RG-Pel/sprint-2-pb-rg-pel) e na [sprint 3](https://github.com/Compass-pb-rasa-2022-RG-Pel/sprint-3-pb-rg-pel) com MongoDB, para armazenamento do histórico de consultas. O bot deve estar apto a dizer se a consulta já foi feita ou não e dar a resposta sem consulta à API.
- Bot-3: Coloque o bot-2 em docker, utilizando docker-compose. Dica: <https://rasa.com/docs/rasa/docker/deploying-in-docker-compose/>
- Bot-4: Coloque o bot-3 em kubernetes no Okteto. Dica: <https://learning.rasa.com/deployment/kubernetes-commands/>

---

## Entrega

- Fazer o clone do repositório da sprint-4-pb-rg-pel;
- Criar uma branch no repositório com o formato nome-sobrenome (Exemplo: daniel-muller);
- Na sua branch, criar uma pasta para cada exercício, no formato bot-número (Exemplo: bot-1);
- Subir o trabalho na branch com um readme.md, documentando detalhes sobre como a avaliação foi desenvolvida e como utilizar o sistema;
- O prazo de entrega é até às 10h do dia 05/07/2022 no repositório do github (<https://github.com/Compass-pb-rasa-2022-RG-Pel/sprint-4-pb-rg-pel>).

---
---

# API Utilizada:

- API.

# Tecnologias Utilizadas:
- Python 
- Rasa 
- Spacy 
- Dotenv
- Pymongo 
- MongoDB
- Docker e docker-compose 
- Okteto

# Chatbot

primeira busca na API. 

# Docker

Foram criados dois arquivos Dockerfile: um para a imagem do server do chatbot e o outro com a imagem do bot. O server.Dockerfile tem a função de executar o "rasa run actions" utilizado no terminal para acessar as actions do bot, além disso, ele precisa fazer a instalação do pymongo para que o bot consiga interagir com o mongoDB. O bot.Dockerfile faz a instalação do spacy para download do pt_core_news_sm. As imagens utilizadas foram utilizadas do DockerHub e foram carregadas em containers, as dependências externas foram instaladas e uma nova imagem era gerada, contendo as dependências externas necessárias. 

# BOT Web

O socket.io foi configurado em credentials.yml e manipulado dentro do main.js para usar o bot treinado com as informações que o usuário digita para ele.

Foi criado mais um arquivo Dockerfile que monta uma imagem para rodar um servidor express, presente no arquivo server.js.

<h3>bot</h3>

<h3>Quando o usuário busca por algo que não está na API</h3>

Link: https://web-evertonlwf.cloud.okteto.net
