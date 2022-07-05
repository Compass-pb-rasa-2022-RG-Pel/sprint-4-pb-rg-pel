# Avaliação Sprint 4- Rasa o inicio do chat bot!

Api midea stack

## Execução

### A escolha desta Api foi pela variedade de informação que ela retorna, assim facilitando o metodo e interação para a criação dos stores.

### Primeiro temos que ter um ambiente vrtual optei pelo conda.

- conda create --name rasaenv python=3.8

### Virtualenv

- virtualenv -p python3.8 rasaenv

### Usar o pipenv

- cd rasa dar entre para entrar na pasta e após pipenv install

### Aqui vc encontra todo o passo a passo da instalação e sua documentação https://rasa.com/docs/rasa/installation/ .

### Após todos os processos de instalação realizados vamos para a parte de treinamento do bot.

### Vamos inicializar os arquivos com alguns comandos.

- rasa init

### Após ter criado todo o processo e estrutura do bot vamos seguir com o treinamento.

- rasa train

### Agora para executar o bot shell

- rasa shell

### Com esse comando damos start no server rasa

- rasa run --cors "*"

### Esse comando ativa as actions para rodar o bot

- rasa run actions

### Sendo que estes ultimos dois comandos precisam estar em um ambiente virtual como sitado assima e com dois terminais diferentes para sua execução para fim de conseguir os treinamentos e demais funções do rasa!

---
# Como foi a montagem e criação do Bot!


### O primeiro Bot-1 foi postado com a parte de treinamento e códigos funcionais.


### O segundo Bot-2 foi incluido a conexão do mongodb e sua conexão e função para salvar o histórico de acesso dos usuários que usaram a comunicação do Bot.


### O terceiro BOt-3 foi incluido os arquivos para a conexão com o Dockerfile.


### o quarto Bot-4 teve a interação e inclução no okteto para a hospedagem e geração do link de acesso do bot funcionando.

# Imagens do chat Bot!

<img src="https://i.ibb.co/ZMTLPtR/bot1.jpg">



<img src="https://i.ibb.co/P9t8fJZ/bot-2.jpg">


<img src="https://i.ibb.co/G9CK1bm/bot3.jpg">



### Conexão do mongo com os links salvos que vem da api!


<img src="https://i.ibb.co/8KB6g31/mongo-express.jpg">


### conexão com o okteto e seus links de acesso a web e ao mongodb.


<img src ="https://i.ibb.co/r3g05pF/okteto-acessos.jpg">



## segue o link do okteto com a função web para o chat bot.

- * https://web-rodrigovaladao01.cloud.okteto.net/


## Aqui o link para acessar o histórico no banco de dados.

- * https://mongo-e-rodrigovaladao01.cloud.okteto.net/





---
---






### Tive alguns problemas com a conexão da parte front onde criei o código com uma interface similar a um chatbot real para o projeto, e então assim com o okteto nos trazendo grande dificuldades de link, onde ele não conseguia fazer a construção da imagens e seu acesso pois não conseguiamos a combinação e defição para rodar com o mongo,dockerfile e okteto simultaneamente, mas após muito esforço e tentativas chegamos ao final e a conclusão.



- 