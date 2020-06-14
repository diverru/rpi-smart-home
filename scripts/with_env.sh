#!/usr/bin/env bash

DIR=$(dirname $0)

set -a
source $DIR/../.env
set +a

"$@"