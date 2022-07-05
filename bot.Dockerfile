FROM rasa/rasa:3.2.1-full

USER root
RUN python -m spacy download pt_core_news_sm

USER 1001