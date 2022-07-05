FROM rasa/rasa-sdk:latest

USER root

RUN pip3 install pymongo[srv]

USER 1001