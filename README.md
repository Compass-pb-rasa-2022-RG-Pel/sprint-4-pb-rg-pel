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

- rasa train

### Agora para executar o bot shell

- rasa shell

### Com esse comando damos start no server rasa

- rasa run cors-- "*"

### Esse comando ativa as actions para rodar o bot

- rasa run actions

### Na pasta web acesse o index.html em seu navegador,onde estará o chatbot para executar.

---





---
---
