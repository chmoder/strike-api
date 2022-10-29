import typing
import json

from base import call_api


def get_subscriptions(
    account_id: typing.Optional[str],
    handle: typing.Optional[str],
) -> dict:
    url = f"https://api.strike.me/v1/subscriptions"

    return call_api("GET", url)


def get_subscription(subscription_id: str) -> dict:
    url = f"https://api.strike.me/v1/subscriptions/{subscription_id}"

    headers = {"Accept": "application/json"}

    return call_api("GET", url, headers=headers)


def create_subscription(
    webhook_url: str,
    webhook_version: str,
    secret: str,
    enabled: bool,
    event_type: typing.List[str],
) -> dict:
    url = "https://api.strike.me/v1/subscriptions"

    payload = json.dumps(
        {
            "webhookUrl": webhook_url,
            "webhookVersion": webhook_version,
            "secret": secret,
            "enabled": enabled,
            "eventTypes": event_type,
        }
    )

    headers = {"Content-Type": "application/json"}

    return call_api("POST", url, headers=headers, data=payload)


def update_subscription(
    subscription_id: str,
    webhook_url: str,
    webhook_version: str,
    secret: str,
    enabled: bool,
    event_type: typing.List[str],
) -> dict:
    url = f"https://api.strike.me/v1/subscriptions/{subscription_id}"

    headers = {"Content-Type": "application/json"}
    payload = json.dumps(
        {
            "webhookUrl": webhook_url,
            "webhookVersion": webhook_version,
            "secret": secret,
            "enabled": enabled,
            "eventTypes": event_type,
        }
    )

    return call_api("PATCH", url, headers=headers, data=payload)


def delete_subscription(subscription_id: str) -> dict:
    url = f"https://api.strike.me/v1/subscriptions/{subscription_id}"

    return call_api("DELETE", url)
