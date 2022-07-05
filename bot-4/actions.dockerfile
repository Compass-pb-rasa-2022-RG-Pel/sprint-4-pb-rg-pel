FROM rasa/rasa-sdk:latest
WORKDIR /app

USER root

RUN pip3 install pymongo[srv]
COPY ./actions /app/actions
