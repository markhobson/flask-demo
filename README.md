# Flask Demo

## Running locally

Create a virtual environment:

```bash
python3 -m venv --prompt . .venv
```

Active the virtual environment:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -e .
```

Run the server:

```bash
flask run
```

Open http://127.0.0.1:5000.

## Formatting and linting

Install the build dependencies:

```bash
pip install -e .[build]
```

Reformat the code:

```bash
black .
```

Organise imports:

```bash
isort .
```

Lint the code:

```bash
pylint app tests
```

Run the static type checker:

```bash
mypy --strict -p app -p tests
```

## Running tests

Install the test dependencies:

```bash
pip install -e .[test]
```

Install the Playwright browsers:

```bash
playwright install
```

Run the tests:

```bash
python -m pytest tests
```
