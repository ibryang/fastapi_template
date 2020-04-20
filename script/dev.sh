#!/usr/bin/env zsh

BIN_DIR=~/myEnv/bin


if [ ! -d "$BIN_DIR" ]; then
  BIN_DIR=~/myEnv/bin

fi

$BIN_DIR/python main.py