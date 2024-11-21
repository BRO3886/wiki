#!/bin/bash

# Navigate to the wiki directory
cd ~/Documents/wiki || exit

# Check if there are changes to commit
if [[ -n $(git status --porcelain) ]]; then
    make all
else
    exit 0
fi
