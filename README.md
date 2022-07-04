# API Utilizada:

- SWAPI: The Star Wars API
O Chatbot utiliza a API SWAPI para buscar informações sobre os episódios dos filmes Star Wars.
Como a API em questão está toda em inglês, o método que usei para que o bot consultasse a API é através dos números dos 6 episódios da franquia original. O usuário indica qual é o número do episódio e o bot faz uma tratativa para repassar a informação que encontrou na API.

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
Charlie é o bot criado para acompanhar o usuário em suas pesquisas sobre os episódios Star Wars. Para iniciar uma conversa basta dar uma breve saudação a ele. Charlie é treinado para saudar e se apresentar ao usuário. Ao iniciar uma nova conversa, o primeiro formulário é aberto, o usuário deve fornecer seu nome para Charlie faça sua primeira busca na API. 

Como a API se limite apenas nos filmes iniciais da saga, Charlie, mostra ao usuário quais episódios ele consegue consultar algumas informações. 

Caso o usuário pesquise por algum filme em específico, ele deve informar o número do episódio desejado. Primeiro, será verificado no banco de dados, MongoDB, se alguém com o nome informado já foi cadastrado pesquisando sobre o título em questão. Se for encontrado algum resultado, ele informará ao usuário quando que ele fez a consulta e as informações obtidas. Se não for encontrado nenhum dado no mongo, ele irá realizar a inserção e mostrar ao usuário as informações que ele encontrou na API.

Charlie é treinado, para informar ao usuário quando não entende algum comando que o usuário passa para ele, pedindo que seja reformulada a frase informada, para que ele possa compreender o desejo do usuário.

# Docker

Foram criados dois arquivos Dockerfile: um para a imagem do server do chatbot e o outro com a imagem do bot. O server.Dockerfile tem a função de executar o "rasa run actions" utilizado no terminal para acessar as actions do bot, além disso, ele precisa fazer a instalação do pymongo para que o bot consiga interagir com o mongoDB. O bot.Dockerfile faz a instalação do spacy para download do pt_core_news_sm. As imagens utilizadas foram utilizadas do DockerHub e foram carregadas em containers, as dependências externas foram instaladas e uma nova imagem era gerada, contendo as dependências externas necessárias. 

# BOT Web
Para que o BOT Charlie pudesse ser acessado fora do localhost, foi criado uma pasta web que constrói um HTML simples, ligado ao socket.io. Através do main.js a página consegue apresentar o mesmo estilo de conversação que o bot no prompt de comando. O socket.io foi configurado em credentials.yml e manipulado dentro do main.js para usar o bot treinado com as informações que o usuário digita para ele.

Foi criado mais um arquivo Dockerfile que monta uma imagem para rodar um servidor express, presente no arquivo server.js.

<h3>Conversa comum com o Charlie</h3>
<img src="https://user-images.githubusercontent.com/105460289/177201101-b63d8d24-6cd4-47f7-8d1c-8767391dab86.png">

<h3>Quando o usuário busca por algo que não está na API</h3>
<img src="https://user-images.githubusercontent.com/105460289/177201921-9a8dcaf7-242e-424e-b704-54b34ba39d3c.png">

Link: https://web-anamasflaviamoraes.cloud.okteto.net
