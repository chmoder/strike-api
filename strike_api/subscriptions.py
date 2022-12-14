import typing
import json

from strike_api.base import call_api
from strike_api.models.subscriptions import Subscription, Subscriptions


def get_subscriptions() -> Subscriptions:
    """Get subscriptions

    Returns:
        Subscriptions: list of subscriptions
    """
    url = f"https://api.strike.me/v1/subscriptions"

    response = call_api("GET", url)
    return Subscriptions.parse_obj(response)


def get_subscription(subscription_id: str) -> Subscription:
    """Get subscription by id

    Args:
        subscription_id (str): id of subscription

    Returns:
        Subscription: subscription
    """
    url = f"https://api.strike.me/v1/subscriptions/{subscription_id}"

    headers = {"Accept": "application/json"}

    response = call_api("GET", url, headers=headers)
    return Subscription.parse_obj(response)


def create_subscription(
    webhook_url: str,
    webhook_version: str,
    secret: str,
    enabled: bool,
    event_type: typing.List[str],
) -> Subscription:
    """Creates a new subscription.  You can create at most 50 subscriptions.

    Args:
        webhook_url (str): Webhook HTTPS endpoint url.
        webhook_version (str): Version that will be used when formatting the webhook payload.
        secret (str): Webhook secret that will be used for signing the request.
        enabled (bool): Flag for enabling/disabling the subscription. If subscription is disabled the webhook won't be triggered for the respective event types.
        event_type (typing.List[str]): List of event types for the subscription. Each time that some event type from the list occurs, the webhook will be triggered.

    Returns:
        Subscription: The created subscription.
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

    response = call_api("POST", url, headers=headers, data=payload)
    return Subscription.parse_obj(response)


def update_subscription(
    subscription_id: str,
    webhook_url: str,
    webhook_version: str,
    secret: str,
    enabled: bool,
    event_type: typing.List[str],
) -> Subscription:
    """Update a subscription.

    Args:
        subscription_id (str): Id of subscription to update.
        webhook_url (str): Webhook HTTPS endpoint url.
        webhook_version (str): Version that will be used when formatting the webhook payload.
        secret (str): Webhook secret that will be used for signing the request.
        enabled (bool): Flag for enabling/disabling the subscription. If subscription is disabled the webhook won't be triggered for the respective event types.
        event_type (typing.List[str]): List of event types for the subscription. Each time that some event type from the list occurs, the webhook will be triggered.

    Returns:
        Subscription: The updated subscription.
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

    response = call_api("PATCH", url, headers=headers, data=payload)
    return Subscription.parse_obj(response)


def delete_subscription(subscription_id: str) -> None:
    """Delete a subscription

    Args:
        subscription_id (str):  Id of subscription to delete

    Returns:
        None
    """
    url = f"https://api.strike.me/v1/subscriptions/{subscription_id}"

    call_api("DELETE", url)
    return None
