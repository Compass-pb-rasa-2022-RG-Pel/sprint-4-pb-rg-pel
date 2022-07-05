# BotCep - Informações sobre o logradouro de um CEP

---
## Descrição do projeto
- A proposta deste projeto é a construção de um chatbot utilizando o framework Rasa, sua principal função é retornar informações referente ao logradouro do CEP informado.
- Seu desenvolvimento será apresentado em 4 etapas, sendo respectivamente uma etapa para cada chatbot desenvolvido, e conforme o incremento de novas tecnologias um novo chatbot é criado.

## Tecnologias utilizadas em todo o projeto
- [Rasa](https://rasa.com)
- [MongoDB](https://www.mongodb.com)
- [Docker](https://www.docker.com)
- [Kubernetes](https://kubernetes.io/pt-br/)
- [Spacy](https://spacy.io) - uso do pacote de idiomas [pt_core_news_sm](https://spacy.io/models/pt)
- [Telegram](https://web.telegram.org/z/)
- [Ngrok](https://ngrok.com)

## Link para acesso via Telegram: ```t.me/PesquisaCep_bot```

---
---

# Bot 1
## Tecnologias utilizadas nesta etapa
- [x] Rasa
- [ ] MongoDB
- [ ] Docker
- [ ] Kubernetes
- [x] Spacy
- [ ] Telegram
- [ ] Ngrok

## Descrição
- Nesta primeira etapa o chatbot é desenvolvido em Português e utilizando a biblioteca Spacy com o pacote de idiomas "pt_core_news_md".
- Sua construção é simples: dentro do caminho "data/" encontramos o arquivo "nlu.yml" esse que contém todas as "intents" ou "inteções" do usuário para com o chatbot. Utilizando das intents o modelo é treinado para previsão da entrada fornecida pelo usuário.
- Os arquivos "rules.yml" e "stories.yml" também encontrados no caminho "data/", definem o fluxo de conversão entre usuário e chatbot.

## Comandos disponíveis

```rasa train```

- Este comando é utilizado para treinar um modelo. Após o treinamento é gerado um arquivo.tar.gz que será utilizado para executar o chatbot.

```rasa run actions```

- Através deste comando será possível executar o servidor responsável pelas actions do chatbot.

```rasa shell```

- Comando utilizado para iniciar a interação com o chatbot. Necessário executar o comando "rasa run actions" antes da execução deste comando.

## Como ele funciona?
- O usuário deve informar seu nome e um CEP o qual deseja descobrir as informações.
- O chatbot retornará as informações via chat caso o CEP seja válido, entretanto, retornará um erro ao usuário caso o CEP não seja valido. 

## Como executar o bot 1?
- Primeiramente é necessário realizar o treinamento para gerar um modelo: utilize o comando "rasa train".
- Após o modelo de treinamento ser gerado é preciso iniciar o servidor das actions com o seguinte comando: "rasa run actions". As actions só serão executadas caso o servidor da mesma esteja em execução.
- Por fim, execute o comando: "rasa shell" para carregar o modelo treinado e interagir com o bot via terminal.

---
---

# Bot 2
## Tecnologias utilizadas nesta etapa
- [x] Rasa
- [x] MongoDB
- [ ] Docker
- [ ] Kubernetes
- [x] Spacy
- [ ] Telegram
- [ ] Ngrok

## Descrição
- Nesta primeira etapa o chatbot é desenvolvido em Português e utilizando a biblioteca Spacy com o pacote de idiomas "pt_core_news_md".
- Sua construção é simples: dentro do caminho "data/" encontramos o arquivo "nlu.yml" esse que contém todas as "intents" ou "inteções" do usuário para com o chatbot. Utilizando das intents o modelo é treinado para previsão da entrada fornecida pelo usuário.
- Os arquivos "rules.yml" e "stories.yml" também encontrados no caminho "data/", definem o fluxo de conversão entre usuário e chatbot.
- No caminho "actions/" é possível identificar o arquivo "actions.py" com uma classe denominada ActionProcuraCep, onde nela é executada a inserção de um CEP novo ou busca de um CEP já armazenado no banco, fazendo com que não se necessite o uso da API.

## Como ele funciona?
- O usuário deve informar seu nome e CEP o qual deseja descobrir as informações.
- O chatbot retornará as informações via chat caso o CEP seja válido, entretanto, retornará um erro ao usuário caso o CEP não seja valido.
- Após a consulta ser realizada os valores retornados ao usuário são armazenados no banco de dados, bem como seu nome e CEP(e suas demais informações) informado no início da conversação.

## Como executar o bot 2?
- Primeiramente é necessário realizar o treinamento para gerar um modelo: utilize o comando "rasa train".
- Após o modelo de treinamento ser gerado é preciso iniciar o servidor das actions com o seguinte comando: "rasa run actions". As actions só serão executadas caso o servidor da mesma esteja em execução.
- Por fim, execute o comando: "rasa shell" para carregar o modelo treinado e interagir com o bot via terminal.

---
---

# Bot 3
## Tecnologias utilizadas nesta etapa
- [x] Rasa
- [x] MongoDB
- [x] Docker
- [ ] Kubernetes
- [x] Spacy
- [x] Telegram
- [x] Ngrok

## Descrição
- Na primeira etapa o chatbot 1 é desenvolvido em Português e utilizando a biblioteca Spacy com o pacote de idiomas "pt_core_news_md".
- Sua construção é simples: dentro do caminho "data/" encontramos o arquivo "nlu.yml" esse que contém todas as "intents" ou "inteções" do usuário para com o chatbot. Utilizando das intents o modelo é treinado para previsão da entrada fornecida pelo usuário.
- Os arquivos "rules.yml" e "stories.yml" também encontrados no caminho "data/" definem o fluxo de conversação entre usuário e chatbot.
- No caminho "actions/" é possível identificar o arquivo "actions.py" com uma classe denominada ActionProcuraCep, onde nela é executada a inserção de um CEP novo ou busca de um CEP já armazenado no banco, fazendo com que não se necessite o uso da API.
- Para a conternização do chatbot é necessário a criação de dois arquivos "dockerfile", esses definem as caracteristicas das imagens utilizadas por cada container, em especifico o arquivo "actions.Dockerfile" possui a necessidade de instalar a dependencia para utilizar o MongoDB, denominada "pymongo", devido a isso no caminho "actions/" é encontrado o "requirements-actions.txt" que armazena o nome das dependencias para instalação na imagem criada.
- O arquivo "docker-compose.yml" é utilizado para osquestrar a construção e interação entre os containers criado
- Nesta etapa utilizamos também a tecnologia do Ngrok para tornar nosso localhost na porta 5005 pública, isso é necessário para a API do Telegram conseguir se comunicar com nossos container.

## Comandos disponíveis

```docker-compose up```

- Este comando é utilizado para construção dos containers utilizados pelo chatbot.

```ngrok http 5005```

- Este é utilizado para criar uma URL pública através do Ngrok.


## Como ele funciona?
- O usuário deve informar seu nome e CEP o qual deseja descobrir as informações.
- O chatbot retornará as informações via chat caso o CEP seja válido, entretanto, retornará um erro ao usuário caso o CEP não seja valido. 
- Após a consulta ser realizada os valores retornados ao usuário são armazenados no banco de dados, bem como seu nome e CEP(e suas informações) informado no início da conversação.
- Os containers "rasa-actions" e "rasa-shell" são responsáveis pela criação das imagens para que com o arquivo "docker-compose.yml" possam executar os comandos de inicialização do servidor de actions e para ativação do interface de comunicação com o Telegram.
- A comunicação com o chatbot deve ser feita via Telegram, basta acessar via: ```t.me/PesquisaCep_bot```

## Como executar o bot 3?
- Primeiramente é necessário realizar o treinamento para gerar um modelo: utilize o comando "rasa train".
- Será necessário configurar o arquivo "credentials.yml" com a URL pública disponibilizada através do Ngrok.
![Ngrok](/src/ngrok.png)
- Através do Ngrok dispare o comando "ngrok http 5005" e após será disponibilizado conforme exemplo acima, uma URL pública.
- A alteração deve ser feita no local onde está disposto a linha vermelha, conforme imagem abaixo. ![Ngrok-credentials](/src/ngrok-credentials.png)
- Após o modelo de treinamento ser gerado basta carregar o "docker-compose.yml" com o comando "docker-compose up", todos os comandos internos serão disparados sozinhos.

---
---

## Bot 4
## Tecnologias utilizadas nesta etapa
- [x] Rasa
- [x] MongoDB
- [x] Docker
- [x] Kubernetes
- [x] Spacy
- [x] Telegram
- [x] Ngrok

## Descrição
- Na primeira etapa o chatbot 1 é desenvolvido em Português e utilizando a biblioteca Spacy com o pacote de idiomas "pt_core_news_md".
- Sua construção é simples: dentro do caminho "data/" encontramos o arquivo "nlu.yml" esse que contém todas as "intents" ou "inteções" do usuário para com o chatbot. Utilizando das intents o modelo é treinado para previsão da entrada fornecida pelo usuário.
- Os arquivos "rules.yml" e "stories.yml" também encontrados no caminho "data/" definem o fluxo de conversação entre usuário e chatbot.
- No caminho "actions/" é possível identificar o arquivo "actions.py" com uma classe denominada ActionProcuraCep, onde nela é executada a inserção de um CEP novo ou busca de um CEP já armazenado no banco, fazendo com que não se necessite o uso da API.
- Para a conternização do chatbot é necessário a criação de dois arquivos "dockerfile", esses definem as caracteristicas das imagens utilizadas por cada container, em especifico o arquivo "actions.Dockerfile" possui a necessidade de instalar a dependencia para utilizar o MongoDB, denominada "pymongo", devido a isso no caminho "actions/" é encontrado o "requirements-actions.txt" que armazena o nome das dependencias para instalação na imagem criada.
- O arquivo "Docker-compose.yml" é utilizado para osquestrar a construção e interação entre os containers criado
- Nesta etapa será utilizado a plataforma Okteto para hospedar a criação de pods, a única mudança desta etapa para etapa anterior é o nome dos arquivos "docker-compose.yml" para "Docker-compose.yml" e os arquivo "credentials.yml" que recebe o valor "https://container-rasa-shell-juanweimar.cloud.okteto.net", esse disponibilizado pelo Okteto.

## Como ele funciona?
- O usuário deve informar seu nome e CEP o qual deseja descobrir as informações.
- O chatbot retornará as informações via chat caso o CEP seja válido, entretanto, retornará um erro ao usuário caso o CEP não seja valido. 
- Após a consulta ser realizada os valores retornados ao usuário são armazenados no banco de dados, bem como seu nome e CEP(e suas informações) informado no início da conversação.
- Os pods são criados a partir dos containers "rasa-actions" e "rasa-shell" são responsáveis pela criação das imagens para que com o arquivo "Docker-compose.yml" possam executar os comandos de inicialização do servidor de actions e para ativação do interface de comunicação com o Telegram.
- A comunicação com o chatbot deve ser feita via Telegram, basta acessar via: t.me/PesquisaCep_bot

## Como executar o bot 4?
- É necessário realizar o treinamento para gerar um modelo antes do deploy dos arquivos na plataforma Okteto.
- Entretanto, o chatbot 4 já se encontra hospedado no Okteto, para acesso basta acessar via: ```t.me/PesquisaCep_bot```


---
---
