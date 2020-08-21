CURRENT_GITHOOKS_FOLDER := $(shell git config --get core.hooksPath)
GITHOOKS_FOLDER := .githooks

init:
ifeq ($(CURRENT_GITHOOKS_FOLDER),)
	chmod 775 .githooks/*
	git config core.hooksPath .githooks
endif
	

run: init
	FLASK_APP=flaskr \
	FLASK_ENV=development \
	flask run

lint: init
	flake8 --exclude .git,__pycache__,.githooks,env,.pytest_cache

test: init
	pytest

install: init
	pip3 install -r requirements.txt