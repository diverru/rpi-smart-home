FROM nginx:latest
ARG DOMAIN

LABEL maintainer="Alexander Kiselyov"

USER root
ENV HOME /root
RUN apt-get update && apt-get install -yy python3

COPY letsencrypt-nginx/resources/nginx.conf /etc/nginx/conf.d/default.conf
COPY letsencrypt-nginx/resources/index.html /usr/share/nginx/html/index.html

COPY subst_env.py /
RUN /subst_env.py /etc/nginx/conf.d/default.conf
