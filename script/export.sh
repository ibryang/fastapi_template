#!/usr/bin/env bash

BIN_DIR=~/myEnv/bin

if [ ! -d "$BIN_DIR" ]; then
  BIN_DIR=~/myEnv/bin
fi

rm -f ./requirements.txt
$BIN_DIR/pip freeze > ./requirements.txt
