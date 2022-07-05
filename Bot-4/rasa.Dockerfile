FROM rasa/rasa-sdk:3.0.2
WORKDIR /app

USER root

COPY ./actions /app/actions

USER root