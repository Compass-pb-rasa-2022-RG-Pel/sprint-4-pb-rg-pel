FROM python:3.8.10-slim

USER root

WORKDIR /app

COPY . .

RUN pip install -r /app/requirements.txt

USER 1001

CMD ["bash"]