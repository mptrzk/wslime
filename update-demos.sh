#!/bin/bash


src=static/wslime.js

for dst in demo/*/wslime.js
do
  cp -v $src $dst
done
