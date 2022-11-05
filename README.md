# strike-python
A python client for the https://strike.me API.  This client uses pydantic and encorages strict typing.  

[![PyPI version](https://badge.fury.io/py/strike-api.svg)](https://badge.fury.io/py/strike-api)
[![Documentation Status](https://readthedocs.org/projects/strike-api/badge/?version=latest)](https://strike-api.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/github/chmoder/strike-api/branch/main/graph/badge.svg?token=JR81BI9IGR)](https://codecov.io/github/chmoder/strike-api)


## Example Usage
`$ export STRIKE_API_KEY=<STRIKE_API_KEY>`
```python
from strike_api import rates

rates = rates.get_ticker()
rates[0].amount
```

## Build strike-api
[Install Poetry](https://python-poetry.org/docs/#installation)
```
python -m pip install --upgrade pip
pip install poetry
poetry install
```

### Build Docs
```
cd docs
poetry run sphinx-apidoc -f -o . ../strike_api
poetry run make clean && poetry run make html
```

### Run Tests
```
poetry run pytest --record-mode=once
```