FROM rasa/rasa-sdk:3.0.2
WORKDIR /app
USER root
RUN pip install pymongo
RUN pip install python-dotenv
COPY ./actions /app/actions
USER root