#!/bin/bash
cd ~/Documents/wiki || exit
if [[ -n $(git status --porcelain) ]]; then
    make all
else
    exit 0
fi
