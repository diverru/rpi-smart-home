#!/usr/bin/env bash

set -e

ROOT=$(realpath $(dirname $0)/../var)
source $ROOT/../.env

docker run -it --rm \
    -v $ROOT/letsencrypt/etc:/etc/letsencrypt \
    -v $ROOT/letsencrypt/var/lib:/var/lib/letsencrypt \
    -v $ROOT/letsencrypt/site:/data/letsencrypt \
    -v $ROOT/logs/letsencrypt:/var/log/letsencrypt \
    certbot/certbot \
    certonly --webroot \
    --agree-tos --no-eff-email --email $EMAIL \
    --webroot-path=/data/letsencrypt \
    --rsa-key-size 4096 \
    -d $DOMAIN

mkdir -p $ROOT/letsencrypt/dh-param
openssl dhparam -out $ROOT/letsencrypt/dh-param/dhparam.pem 4096
