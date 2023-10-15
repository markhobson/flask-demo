black:
	black app tests

isort:
	isort app tests

format: black isort

mypy:
	mypy --strict -p app -p tests

pylint:
	pylint app tests

lint: mypy pylint

test:
	python -m pytest tests
