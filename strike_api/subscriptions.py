import typing
import json

from strike_api.base import call_api


def get_subscriptions() -> typing.List[dict]:
    """Get subscriptions

    Returns:
        typing.List[dict]: list of subscriptions
    """

    url = f"https://api.strike.me/v1/subscriptions"

    return call_api("GET", url)


def get_subscription(subscription_id: str) -> dict:
    """Get subscription by id

    Args:
        subscription_id (str): id of subscription

    Returns:
        dict: subscription
    """
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
    """Create a new subscription

    You can create at most 50 subscriptions

    Args:
        webhook_url (str): Webhook HTTPS endpoint url.
        webhook_version (str): Version that will be used when formatting the webhook payload.
        secret (str): Webhook secret that will be used for signing the request.
        enabled (bool): Flag for enabling/disabling the subscription. If subscription is disabled the webhook won't be triggered for the respective event types.
        event_type (typing.List[str]): List of event types for the subscription. Each time that some event type from the list occurs, the webhook will be triggered.

    Returns:
        dict: subscription
    """
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
    """Update a subscription

    Args:
        subscription_id (str): Id of subscription to update.
        webhook_url (str): Webhook HTTPS endpoint url.
        webhook_version (str): Version that will be used when formatting the webhook payload.
        secret (str): Webhook secret that will be used for signing the request.
        enabled (bool): Flag for enabling/disabling the subscription. If subscription is disabled the webhook won't be triggered for the respective event types.
        event_type (typing.List[str]): List of event types for the subscription. Each time that some event type from the list occurs, the webhook will be triggered.

    Returns:
        dict: _description_
    """
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
    """Delete a subscription

    Args:
        subscription_id (str): Id of subscription to update

    Returns:
        dict: subscription
    """
    url = f"https://api.strike.me/v1/subscriptions/{subscription_id}"

    return call_api("DELETE", url)
