
init:
	git config core.hooksPath .githooks

run:
	FLASK_APP=flaskr \
	FLASK_ENV=development \
	flask run

lint:
	flake8 --exclude .git,__pycache__,.githooks,env,.pytest_cache

test:
	pytest