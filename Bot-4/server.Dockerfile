# Utiliza a imagem rasa-sdk oficial como base
FROM rasa/rasa-sdk:3.2.1
WORKDIR /app

# Copia para o container arquivo que define as dependências externas
COPY actions/requirements-actions.txt ./

# Utiliza o root user para instalar as dependências
USER root

# Instala as dependências
RUN pip install -r requirements-actions.txt

# Copia as actions para o workdir
COPY ./actions /app/actions

RUN pip install nltk
RUN python -m nltk.downloader punkt
COPY ./tokenizers /root/nltk_data/tokenizers
