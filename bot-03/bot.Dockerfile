FROM rasa/rasa:latest-full

# Utiliza o root user para instalar as dependências
USER root

# Instala as dependências
RUN pip3 install -U spacy 
RUN python -m spacy download pt_core_news_md

# Seguindo as boas práticas não executo o código com user root
USER 1001