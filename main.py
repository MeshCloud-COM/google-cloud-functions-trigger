import os
import requests

from requests.auth import HTTPBasicAuth

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PROM_USER = os.getenv("PROM_USER")
PROM_PASS = os.getenv("PROM_PASS")

AUTH = HTTPBasicAuth(PROM_USER, PROM_PASS)


def triggered_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    headers = {'Content-Type': 'application/json'}
    payload_message = event

    resp = requests.post(WEBHOOK_URL, json=payload_message, headers=headers, auth=AUTH)

    return f'ok'


def triggered_http(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    payload_message = request.get_json()

    headers = {
        'Content-Type': 'application/json'
    }

    resp = requests.post(WEBHOOK_URL, json=payload_message, headers=headers, auth=AUTH)

    return f'ok'
