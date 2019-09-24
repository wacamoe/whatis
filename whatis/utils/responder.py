from requests import post
from slack.web.classes import messages


def webhook_response(response_url: str, json=None):
    return post(response_url, json=json)


def basic_responder_response(text: str) -> messages.Message:
    return messages.Message(text=text)
