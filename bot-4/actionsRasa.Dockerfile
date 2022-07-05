FROM rasa/rasa-sdk:3.0.2
WORKDIR /app
USER root
RUN pip3 install pymongo
COPY ./actions /app/actions
USER root