# Avaliação Sprint 4 - Programa de Bolsas Compass.uol e universidades de Rio Grande e Pelotas
Avaliação da quarta sprint do programa de bolsas Compass.uol para formação em chatbot Rasa.

---

# CatAPI - Consulta a raça do gato

### Descrição do projeto


* O projeto executa a constução de um chatbot utilizando o framework Rasa, com a principal função de retornar a foto de um gato referente a consulta pela raça.

* O desenvolvimento do projeto está apresentado em 4 etapas, conforme o incremento dos requisitos desenvolvidos

### Tecnologias utilizadas


* Rasa

* Node.js - node-express

* MonoDB

* Docker

* Kubernetes - Okteto


## bot-1

Para o desenvolvimento do bot 1, foi utilizado as seguintes tecnologias:

* Rasa

* Node.js

### Descrição:

Foi desenvolvido um bot em Português (pt-br), sua construção foi simples, editando o arquivo nlu.yml, traduzindo todas as intents para o português, inserindo novas intents e configurando o documento config.yml para pt-br.

### Funcionamento:

Inicia-se a conversa com uma saudação. O bot responde perguntando o nome, o usuario insere o nome, o bot pergunta sobre o que procura, o usuário irá responder que procura por um gato, em seguida o bot pergunta qual a raça desejada, quando o usuário responde qual a raça, o bot retorna com o nome do usuário, o link e a imagem da raça do gato procurado.

## bot-2

### Tecnologias utilizadas

* Rasa

* Node.js

* MongoDB

### Descrição

* Seguir descrição do bot-1.

* Foi adicionado imports para que o MongoDB fosse conectado.

### Dificuldades encontradas

* O import do dotenv executado com sucesso. A idéia era esconder as credenciais do banco de dados, mas não consegui configurar com exito

## bot-3

### Tecnologias utilizadas

* Rasa

* Node

* MongoDB

* Docker

### Descrição

* Seguir descrição bot-2

* Para desenvolver os containers do bot-3, foi necessário a criação de três arquivos dockerfile, um para as actions, outro para o rasa, e outro para o banco MongoDB.

* Foi criado também o arquivo docker-compose.yml, para que os arquivos dockerfile possam ser executados ordenadamente.

## bot-4

### Tecnologias Utilizadas

* Rasa

* Node

* Docker

* Kubernetes - Okteto

### Descrição

* Seguir descrição bot-3

* Nessa etapa será utilizado o Okteto para apresentar o chat em funcionamento.

### Executando localmente:
* Fazer o treinamento: rasa train
* Iniciar servidor das actions: rasa run actions
* Iniciar servidor rasa: rasa run --cors "*"
* Iniciar servidor node

Link: https://web-suelen-prs.cloud.okteto.net/

![Captura de tela de 2022-07-05 05-47-30](https://user-images.githubusercontent.com/29054252/177289248-67aa5a8c-501c-4b81-8e6e-d46007a7f32c.png)





