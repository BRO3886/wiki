.PHONY: all

all: 
	make commit
	make push

commit:
	git add .
	git commit -m "`date +'%Y-%m-%dT%H:%M:%S'`"

push:
	git push origin main