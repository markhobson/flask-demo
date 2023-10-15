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
pip install -e .[dev]
```

Run the server:

```bash
flask run
```

Open http://127.0.0.1:5000.

## Formatting and linting

Reformat the code:

```bash
make format
```

Lint the code:

```bash
make lint
```

## Running tests

Install the Playwright browsers:

```bash
playwright install
```

Run the tests:

```bash
make test
```
