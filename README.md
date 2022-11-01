# strike-python
A python client for the https://strike.me API.  

[![PyPI version](https://badge.fury.io/py/strike-api.svg)](https://badge.fury.io/py/strike-api)
[![Documentation Status](https://readthedocs.org/projects/strike-api/badge/?version=latest)](https://strike-api.readthedocs.io/en/latest/?badge=latest)


## Example Usage
`$ export STRIKE_API_KEY=<STRIKE_API_KEY>`
```python
from strike_api import rates

rates = rates.get_ticker()
```

## Build strike-api
[Install Poetry](https://python-poetry.org/docs/#installation)
```
python -m pip install --upgrade pip
pip install poetry
poetry install
```

## Build Docs
```
poetry run sphinx-apidoc -f -o ./docs ../strike_api
cd docs && poetry run make clean && poetry run make html
```