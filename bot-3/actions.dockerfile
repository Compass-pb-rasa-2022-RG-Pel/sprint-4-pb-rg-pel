FROM rasa/rasa-sdk:latest

USER root

RUN pip3 install pymongo

USER 1001