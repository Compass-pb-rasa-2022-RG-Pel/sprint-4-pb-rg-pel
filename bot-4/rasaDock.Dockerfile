FROM rasa/rasa:3.2.1
USER root
RUN pip3 install spacy
RUN python -m spacy download pt_core_news_sm
USER 1001