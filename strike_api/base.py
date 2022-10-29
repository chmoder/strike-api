import os
import requests

def call_api(method, url, headers=None, data=None):
    strike_api_key = os.environ.get("STRIKE_API_KEY")
    if not strike_api_key:
        raise EnvironmentError("STRIKE_API_KEY not found in environment variables")

    if not headers:
        headers = {}

    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {strike_api_key}"

    response = requests.request(method, url, headers=headers, data=data)

    return response.json()
