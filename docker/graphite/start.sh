#!/usr/bin/env bash


/sbin/my_init &
sleep 10
/configure.py $1
wait