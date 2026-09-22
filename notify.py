import requests

WEBHOOK_URL = "https://hooks.slack.com/services/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"

def send_alert(message):
    payload = {"text": message}
    requests.post(WEBHOOK_URL, json=payload)
