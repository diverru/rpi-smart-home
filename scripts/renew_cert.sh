#!/usr/bin/env bash

set -e

ROOT=$(realpath $(dirname $0)/../var)
source $ROOT/../.env

docker run --rm -it --name certbot \
    -v $ROOT/letsencrypt/etc:/etc/letsencrypt \
    -v $ROOT/letsencrypt/var/lib:/var/lib/letsencrypt \
    -v $ROOT/letsencrypt/site:/data/letsencrypt \
    -v $ROOT/logs/letsencrypt:/var/log/letsencrypt \
    certbot/certbot renew --quiet --rsa-key-size 4096
