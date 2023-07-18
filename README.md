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

## Linting

Install the build dependencies:

```bash
pip install -e .[build]
```

Run the static type checker:

```bash
mypy --strict .
```

## Running tests

Install the test dependencies:

```bash
pip install -e .[test]
```

Run the tests:

```bash
python -m pytest tests
```
