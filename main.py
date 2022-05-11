import base64

import requests
from requests.auth import HTTPBasicAuth

WEBHOOK_URL = "https://xxxxxxxxxxxxx"
PROM_USER = "test_user"
PROM_PASS = "test_pass"
AUTH = HTTPBasicAuth(PROM_USER, PROM_PASS)


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    content = base64.b64decode(event['data']).decode('utf-8')

    payload_message = {
        "msg_type": "text",
        "content": content
    }

    headers = {
        'Content-Type': 'application/json'
    }

    resp = requests.post(WEBHOOK_URL, json=payload_message, headers=headers, auth=AUTH)

    return f'ok'

