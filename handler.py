import json
import requests
import os


headers = {"Content-type": "application/json", "Authorization": "Bearer " + os.environ["SLACK_TOKEN"]}

def send_message(message):
    body = {
        "channel": get_channel_id(),
        "text": message,
        "link_names": True
    }
    response = requests.post("https://slack.com/api/chat.postMessage", json=body, headers=headers)

    return {
        "status": response.status_code,
        "reason": response.text
    }

def send_daily_message(event, context):
    daily_message = """@here Bonjour à tous, c'est bientôt l'heure du daily !

Pour rendre le point efficace, répondez à ces trois questions en réponse à ce message :

- Qu'est-ce que j'ai fait hier ?
- Qu'est-ce que je fais aujourd'hui ?
- Quels soucis j'anticipe pour ma journée ?

On se retrouve à 9h30 :)
    """

    return send_message(daily_message)

def send_daily_mail_message(event, context):
    daily_mail_message = """@here Et pour aider le rédacteur du daily mail, remplissez la google sheet suivante : https://docs.google.com/spreadsheets/d/1ffVvOTIw2fPID_4lRDyOa2v0q_TnuOkWZGU4F2LjHoQ/edit#gid=0

Bonne journée !
    """

    return send_message(daily_mail_message)


def get_channel_id():
    return next(
        channel["id"]
        for channel in requests.get("https://slack.com/api/conversations.list", headers=headers).json()["channels"]
        if channel["name"] == os.environ["TEAM_CHANNEL_NAME"]
    )
