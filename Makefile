.PHONY: all

all: 
	make commit
	make push

commit:
	git add .
	git commit -m "update `date +'%Y-%m-%dT%H:%M:%S'`"

push:
	git push origin main

.DEFAULT_GOAL := all