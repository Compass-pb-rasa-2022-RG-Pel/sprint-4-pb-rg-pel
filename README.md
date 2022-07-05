# INICIO
# Avaliação Sprint 4 - Programa de Bolsas Compass.uol e universidades de Rio Grande e Pelotas
Avaliação da quarta sprint do programa de bolsas Compass.uol para formação em chatbot Rasa.

---
<p align="center">
    <a href="#da-atividade-proposta"> Atividade Proposta </a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#do-rasa-chatbot"> Rasa Chatbot </a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#do-mongodb"> Mongo DB </a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#do-okteto"> Okteto </a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#dificuldades-encontradas"> Dificuldades Encontradas </a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="#da-aplicacao"> Aplicação </a>&nbsp;
</p>

---
<br>

![image](https://user-images.githubusercontent.com/90530503/177312313-00f56c31-9a81-43b6-91d4-ab79e80a682e.png)


## DA ATIVIDADE PROPOSTA
<br>

- A atividade da sprint 4 consistia, basicamente, em criar um chatbot Rasa em Português que utilizasse formulário para extrair alguns dados do usuário, que estes dados e os de consultas fossem gravados em slots e que fosse consumida alguma api pública.

- Outra exigência da atividade dessa sprint dizia respeito ao armazenamento dos dados registrados e consultas feitas em banco de dados, mais especificamente o banco de dados MongoDB.

- Exigiu-se dessa tarefa a utilização do docker-compose e, também, que o bot fosse postado no Okteto utilizando kubernetes.

<br>

[Subir ao Início](#inicio)

## DO RASA CHATBOT
<br>

- O Rasa ChatBot é uma ferramenta open source muito poderosa que aplica técnicas de machine learning, inteligência artificial à serviço da melhor experiência em conversação. Essa ferramenta utiliza a linguagem Python e possui fácil integração com diversas plataformas, dentre elas o Facebook, o Whatsapp, o Telegram, a Web e muito mais.

![image](https://user-images.githubusercontent.com/90530503/177316198-61f67ffe-6555-44e0-b3e7-48557b409866.png)

https://rasa.com/

<br>

[Subir ao Início](#inicio)

## DO MONGODB
<br>

- A conexão com o banco de dados foi realizada de forma bastante singela, na classe Habilidades (que é basicamente onde os dados que precisam ser salvos vão aparecer), utilizei os comandos para criar o banco de dados e a collection:

```py

try:
    client = MongoClient("mongodb://root:root@mongodb:27017/")
    database = client["sprint4"]
    minha_colecao = database["pokemons"]
except:
    print("Não foi possível conectar ao banco de dados")
            
```

- Os dados são armazenados através dos comandos:

```py

registro = [{"usuario": usuario, "pokemon": nome, "vida": vida, "ataque": ataque, "defesa": defesa, "ataque especial": ataque_especial, "defesa especial": defesa_especial, "velocidade": velocidade, "imagem": link_foto}]
            
minha_colecao.insert_many(registro) 

```

- Importante destacar que os dados retornam caso o usuário de mesmo nome já tenha consultado o mesmo pokemon, neste caso aparecerá a mensagem de que a consulta já foi feita, isso é garantido com o comando:

```py

if int(minha_colecao.count_documents({"usuario": usuario, "pokemon": pokemon})) > 0:
    dispatcher.utter_message(text=f"Você já consultou o pokemon {pokemon}") 
    
```

- A imagem abaixo ilustra o retorno supramencionado:

![image](https://user-images.githubusercontent.com/90530503/177314815-4b6d2ed6-2b93-4fe0-b18d-c65b5defd782.png)

<br>

[Subir ao Início](#inicio)

### MONGO EXPRESS
<br>

- Optei por utilizar o Mongo Express para melhor visualizar os dados registrados no banco de dados MongoDB. Ele é dinâmico, rápido e bastante leve, um ótimo sistema para utilizar no Okteto.

![image](https://user-images.githubusercontent.com/90530503/177312561-458aee70-18ab-434d-a9a2-2faf55611c95.png)

<br>

[Subir ao Início](#inicio)

## DO OKTETO
<br>

- Para conexão junto ao Okteto, optei por utilizar o docker-compose associado a outros arquivos dockerfile que propiciaram a instalação segura e rápida das aplicações necessárias.

```

version: '3.0'
services:
  chatbot:
    build:
      context: .
      dockerfile: bot.Dockerfile
    container_name: rasa
    networks:
      - rasa-network
    ports:
      - 5005:5056
    volumes:
      - ./:/app
    public: true
    command:
      - run
      - --enable-api
      - --cors
      - "*"
      - --debug
      - -p 5056
  action-server:
    build:
      context: .
      dockerfile: server.Dockerfile
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
      context: ./webchat
      dockerfile: web.Dockerfile
    image: webchat
    container_name: webchat-app
    depends_on:
      - "chatbot"
    networks:
      - rasa-network
    ports:
      - 8080:8080
  mongo-e:
    image: mongo-express
    networks:
      - rasa-network
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: root
      ME_CONFIG_MONGODB_URL: "mongodb://root:root@mongodb:27017/"
networks:
  rasa-network:
    driver: bridge

```

- Pelo documento acima é fácil perceber que utilizei o docker-compose para subir, basicamente, 5 aplicações distintas em uma única rede que chamei de 'rasa-network'.

- As aplicações mencionadas foram o MongoDB, o Mongo Express, a aplicação Web, o ChatBot e o Action-Server.

- Esses três últimos, denominações minhas para:

a) Aplicação Web: Referente ao index.html, o chat-bot web que está diretamente ligado ao 'ChatBot' pelo caminho do próprio Okteto.

b) ChatBot: Refere-se a aplicação externa do Rasa, que possui o modelo treinado e realiza a ponte entre a aplicação Web e as Actions.

c) Action-Server: Assim denominado o conjunto de recursos capaz de se comunicar com o banco de dados, consumir api, funções e métodos em código Python. 

<br>

Segue o link dos dockerfiles mencionados no arquivo acima:

[Aplicação do Chatbot](https://github.com/Compass-pb-rasa-2022-RG-Pel/sprint-4-pb-rg-pel/blob/anderson-oliveira/bot.Dockerfile)

[Aplicação Action-Server](https://github.com/Compass-pb-rasa-2022-RG-Pel/sprint-4-pb-rg-pel/blob/anderson-oliveira/server.Dockerfile)

[Aplicação Web](https://github.com/Compass-pb-rasa-2022-RG-Pel/sprint-4-pb-rg-pel/blob/anderson-oliveira/webchat/web.Dockerfile)

<br>

[Subir ao Início](#inicio)

## DIFICULDADES ENCONTRADAS
<br>

- Impende destacar que, mais uma vez, as maiores dificuldades encontradas ficaram por conta da compatibilidade com o serviço Okteto. Mais precisamente quanto a configuração das portas e de serviços externos. Embora não haja vasta documentação que facilite a elucidação e solução destes problemas, encontramos algumas soluções e as adaptamos aos nossos sistemas. Falo no plural porque embora essa fosse uma tarefa individual, todos os participantes dessa sprint se ajudaram e, assim, conseguimos chegar em um modelo que comportasse todos os serviços necessários em um único docker-compose e completamente sincronizados.

<br>

[Subir ao Início](#inicio)

## DA APLICACAO
<br>

O link da aplicação web segue:<br>
[Aplicação Online no Servidor OKTETO](https://web-andersonaoliveira.cloud.okteto.net/)
---

### Recursos Utilizados

- [Anaconda](https://www.anaconda.com/)
- [Python 3.8](https://www.python.org/downloads/release/python-380/)
- [RASA](https://rasa.com/)
- [NODEJS](https://nodejs.org/en/)
- [VISUAL STUDIO CODE](https://code.visualstudio.com/)
- [MONGO DB](https://www.mongodb.com/)
- [PYMONGO](https://pymongo.readthedocs.io/en/stable/)
- [DOCKER](https://www.docker.com/)
- [KUBERNETES](https://kubernetes.io/pt-br/)
- [REQUESTS](https://pypi.org/project/requests/)
- [API POKEMON](https://pokeapi.co/)
- [OKTETO](https://www.okteto.com/)

<br>

### O que faz?

- Vale destacar que a aplicação efetivamente apenas cumpre todos requisitos necessários para atividade dessa sprint, ela possui formulário em que salva em Slots o nome do usuário e, também, o nome do pokemon consultado. Ela consome uma api pública e, caso encontre, sava as informações em banco de dados MongoDB e as exibe ao usuário. A aplicaão consulta o banco de dados para informar o usuário se ele já consultou aquele determinado pokemon e tudo isso é feito via Web através de aplicação lançada via docker-compose e kubernetes na plataforma Okteto.

- Da aplicação em si, posso apontar algumas soluções eficientes, dentre elas listar o nome de absolutamente todos pokemons em arquivo NLU, dessa forma não existe muita possibilidade do usuário não encontrar o pokemon que procura. Também destaco a vantagem da linguagem Python sobre o Javascript que além de economizar muitas linhas de código para escrever as mesmas coisas, entregou de forma muito mais legível.

<br>

[Subir ao Início](#inicio)
