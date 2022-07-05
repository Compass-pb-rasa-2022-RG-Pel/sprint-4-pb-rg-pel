# Avaliação Sprint 4- Rasa o inicio do chat bot!

Api midea stack

## Execução

### A escolha desta Api foi pela variedade de informação que ela retorna, assim facilitando o metodo e interação para a criação das stores.

### primeiro temos que ter um ambiente vrtual optei pelo conda.

- conda create --name rasaenv python=3.8

### virtualenv

- virtualenv -p python3.8 rasaenv

### usar o pipenv

- cd rasa dar entre para entrar na pasta e após pipenv install

### aqui vc encontra todo o passo a passo da instalação e sua documentação https://rasa.com/docs/rasa/installation/ .

### Após todos os processos de instalação realizados vamos para a parte de treinamento do bot.

### Vamos inicializar os arquivos com alguns comandos.

- rasa init

### Após ter criado todo o processo e estrutura do bot vamos seguir com o treinamento

- rasa train

### Agora para executar o bot shell

- rasa shell

### Com esse comando damos start no server rasa

- rasa run --cors "*"

### Esse comando ativa as actions para rodar o bot

- rasa run actions

### Na pasta web acesse o index.html em seu navegador,onde estará o chatbot para executar.

---
# Como foi a montagem e criação do Bot!


### O primeiro Bot-1 foi postado com a parte de treinamento e codigos funcionais.


### O segundo Bot-2 foi incluido a conexão do mongodb e sua conexão e função para salvar o historico de acesso dos usuarios que usaram a comunicação do Bot.


### o terceiro BOt-3 foi incluido os arquivos para a conexão com o Docker.


### o quarto Bot-4 teve a interação e inclução no okteto para a hospedagem e geração do link de acesso do bot funcionando.

# Imagens do chat Bot!

<img src="https://i.ibb.co/ZMTLPtR/bot1.jpg">

<img src="https://i.ibb.co/P9t8fJZ/bot-2.jpg">

### Conexão do mongo com os links salvos que vem da api!

<img src="https://i.ibb.co/rk9ZMn8/conex-o-do-mongo.jpg">



---
---
### Tive alguns problemas com a conexão da parte front onde criei o codigo com uma interface similar a um chatbot real para o projeto, e então assim com o okteto nos trazendo grande dificuldades de link, onde ele não conseguia fazer a construção da imagens e seu acesso.
- 