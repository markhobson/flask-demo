black:
	black app tests

isort:
	isort app tests

format: black isort

black-check:
	black --check app tests

isort-check:
	isort --check app tests

format-check: black-check isort-check

mypy:
	mypy --strict -p app -p tests

pylint:
	pylint app tests

lint: mypy pylint

test:
	pytest tests

verify: format-check lint test
