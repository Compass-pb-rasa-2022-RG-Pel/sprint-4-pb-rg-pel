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

- [Adviceslip](https://api.adviceslip.com/)
- [libretranslate](https://libretranslate.com/)

# Tecnologias Utilizadas:
- Python 
- Rasa 
- Spacy 
- Dotenv
- Pymongo 
- MongoDB
- Docker e docker-compose 
- Okteto

# Bot

O Bot desenvolvido possui as funcionalidades de exibir conselhos em diferentes idiomas e persistir as consultas no banco de dados [mongo](https://www.mongodb.com/).

# web

O desenvolvimento foi realizado em NodeJs com o framework [Express](https://expressjs.com/pt-br/), é foi utilizado para a comunicação com o server rasa o socket.io onde foi necessário configurar o arquivo credentials.yml.

# Criação do Chatbot

O desenvolvimento do chatbot foi realizado com o framework [Rasa](https://rasa.com/) sequindo os passo disponibilizados na documentação.

# Docker-compose

Para colocar a aplicação no [Okteto](https://www.okteto.com/) foi utilizado o arquivo docker-compose.

```python
    version: '3.0'
    services:

      chatbot:
        build:
          context: .
          dockerfile: ./Rasa-bot1/Rasa.dockerfile
        container_name: rasa
        networks: 
          - rasa-network
        ports:
          - 5005:5056
        depends_on:
          - "actions"
        volumes:
          - ./Rasa-bot1:/app
        command:
          - run
          - --enable-api
          - --cors
          - "*"
          - --debug
          - -p 5056
          - --model
          - models
    

      actions:
        build:
          context: .
          dockerfile: ./Rasa-bot1/Actions.dockerfile
        image: rasa-action-server
        container_name: actions
        networks: 
          - rasa-network
        ports:
          - "5055:5055"
        volumes:
          - "./actions:/app/actions"

      mongodb:
        image: mongo
        container_name: db
        networks: 
          - rasa-network
        ports:
          - 27017:27017
        environment:
          MONGO_INITDB_ROOT_USERNAME: root
          MONGO_INITDB_ROOT_PASSWORD: root
          MONGO_INITDB_DATABASE: sprint4

      web:
        build:
          context: ./chat
          dockerfile: Web.dockerfile
        image: webchat
        container_name: chat
        depends_on:
          - "chatbot"
        networks: 
          - rasa-network
        ports: 
          - 8080:8080

    networks: 
        rasa-network:
            driver: bridge
```
# Dificuldades encontradas

O servidor Rasa no okteto não abre a url pública quando configurada para a porta padrão 5005, onde foi necessário realizar bind para outra porta.  

# Link aplicação

Link: https://web-evertonlwf.cloud.okteto.net
