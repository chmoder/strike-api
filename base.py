import os
import requests

def call_api(method, url, headers=None, data=None):
    token = os.environ["TOKEN"]

    if not headers:
        headers = {}

    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    response = requests.request(method, url, headers=headers, data=data)

    return response.json()
