FROM rasa/rasa-sdk:latest
WORKDIR /app

# Copia para o container arquivo que define as dependências externas
COPY actions/requirements-actions.txt ./

# Utiliza o root user para instalar as dependências
USER root

# Instala as dependências
#RUN pip install -r requirements-actions.txt
RUN pip3 install pymongo[srv]


# Copia as actions para o workdir
COPY ./actions /app/actions

# Seguindo as boas práticas não executo o código com user root
USER 1001
#USER 1001