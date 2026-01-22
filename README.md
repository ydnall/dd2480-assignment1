# DD2480 Software Engineering Fundamentals

This repository contains coursework for DD2480, with the implementation for assignment 1
living under `assignment1/`.

## Quick start (Docker)

```
docker build -t dd2480 .
docker run --rm dd2480
```

## Local setup (venv)

```
cd assignment1
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
PYTHONPATH=src python -m pytest
```

## CI

GitHub Actions runs tests and linting on pushes and pull requests to `main` using Python 3.10.
