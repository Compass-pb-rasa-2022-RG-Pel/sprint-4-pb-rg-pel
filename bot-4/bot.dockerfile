FROM rasa/rasa:latest-full

USER root

RUN pip3 install -U spacy
RUN python3 -m spacy download pt_core_news_md

USER 1001

