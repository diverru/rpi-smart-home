FROM nginx:latest
ARG DOMAIN

LABEL maintainer="Alexander Kiselyov"

USER root
ENV HOME /root
RUN apt-get update && apt-get install -yy python3

COPY nginx/resources/nginx.conf /etc/nginx/nginx.conf
COPY nginx/resources/site.conf /etc/nginx/sites-available/default
COPY nginx/resources/common-ssl.conf /etc/nginx/sites-available/
COPY nginx/resources/common-routes.conf /etc/nginx/sites-available/
COPY subst_env.py /
RUN cd /etc/nginx/sites-available && /subst_env.py ./default
