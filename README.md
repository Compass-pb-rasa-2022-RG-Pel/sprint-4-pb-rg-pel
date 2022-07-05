# API Utilizada:

- NASA: Mars Rovers Photos API
O Chatbot utiliza a API Mars Rovers Photos para buscar uma foto do rover Curiosity através da data em que a foto "chegou na terra", como o link de consulta utiliza o formato AA-MM-DD, no arquivo de action através do código: 

- >  array = earth_date.split("/")
- >  new_date = array[2] + "-" + array[1] + "-" + array[0]
- >  print(new_date)

# Tecnologias Utilizadas:
- Python 
- Rasa 
- Spacy 
- Pymongo 
- MongoDB
- Docker e docker-compose 
- Okteto

# Chatbot
o bot criado para simplesmente realizar um cadastro do nome de um usuario qualquer e mostrar uma foto tirada pelo Curiosity. Para iniciar uma conversa basta dar uma breve saudação a ele. Ao iniciar uma nova conversa, o primeiro formulário é aberto, o usuário deve fornecer seu nome para que o bot faça sua primeira busca na API. 

Como é um protótipo, não foi feita tratativas para garantir que existe uma foto na data pesquisada, muito menos impedir o usuario de digitar uma data invalida. o fluxo de conversação se limitou apenas a apresentacao, cadastramento do nome do usuario e a data de foto solicitada. realizando o procedimento solicitado na avaliação de, ao um usuario repetir uma requisição, o bot indenficar a solicitação no banco de dados e retornar a busca com a mensagem "você já pesquisou a foto dessa data".

# Docker

Foram criados dois arquivos Dockerfile: um para a imagem do server do chatbot e o outro com a imagem do bot. O **server.dockerfile** tem a função de executar o "rasa run actions" utilizado no terminal para acessar as actions do bot, além disso, ele precisa fazer a instalação do **pymongo** para que o bot consiga interagir com o mongoDB. O **bot.dockerfile** faz a instalação do **spacy** e o download do *pt_core_news_sm*. As imagens utilizadas foram utilizadas do DockerHub e foram carregadas em containers, as dependências externas foram instaladas e uma nova imagem era gerada, contendo as dependências externas necessárias. 

# BOT Web
Para que o BOT pudesse ser acessado fora do localhost, foi criado uma pasta webchat que constrói um HTML simples, obtido da propria documentaçao do RASA, ligado ao **socket.io**. O socket.io foi configurado em credentials.yml e manipulado dentro do index.html para usar o bot treinado com as informações que o usuário digita para ele.

# Dificuldades Encontradas
##  Ajustar Rules e Stories
Após diversos erros por conflitos entre as **Rules** e **Stories** foi definido esse ultimo apenas para realizar a saudação, deixando o restante da linha de conversação no arquivo **Rules** onde todos os parametros de **Forms** e **actions** ficaram definidos.
##  Forms e Slots
no decorrer dos treinamentos o **Forms** apresentava erro no terminal, depois de pesquisar e revisar o codigo foi encontrado um problema nos **Slots** (entre as linhas 44 e 54 do *domain.yml*) onde a *entity* estava com erro de identação que não era apontado como erro, porém por estar alinhado com o *type* e *mappings* perdia a função dentro do **Slot** e retornava o erro ao solicitar o mesmo no **Forms**.
##  Configurações com o Okteto

para configurar com o Okteto e utilizar a aplicação web, alguns ajustes foram necessários. No **docker-compose** foi necessário utilizar a porta 5056 para habilitar o bot online. Nos arquivos **bot.dockerfile**, **server.dockerfile** e **docker-compose** foi preciso garantir a importação do RASA na ultima versão (latest). além destes ajustes, no **server.dockerfile** foi direcionado o arquivo *requirements-actions* para garantir o funcionamento do *pymongo* nas actions.


clique [aqui](https://web-vtellesrg.cloud.okteto.net/) para acessar o chatbot
