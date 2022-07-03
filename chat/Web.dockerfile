
FROM node:latest
COPY . /var/www 
WORKDIR /var/www
RUN npm install
ENTRYPOINT node server.js
EXPOSE 3000