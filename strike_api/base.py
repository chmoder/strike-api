import os
import requests

def call_api(method, url, headers=None, data=None):
    token = os.environ.get("TOKEN")
    if not token:
        raise EnvironmentError("TOKEN not found in environment variables")

    if not headers:
        headers = {}

    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    response = requests.request(method, url, headers=headers, data=data)

    return response.json()