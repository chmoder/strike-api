# strike-python
A python client for the https://strike.me API

### Developer Documentation

[Install Poetry](https://python-poetry.org/docs/#installation)
```
python -m pip install --upgrade pip
pip install poetry
poetry install
```

## Build Docs
poetry run sphinx-apidoc -F -o ./docs ../strike_api
poetry run make clean && poetry run make html