import json
import requests
import os


headers = {"Content-type": "application/json", "Authorization": "Bearer " + os.environ["SLACK_TOKEN"]}

def send_daily_message(event, context):
    daily_message = """@here Bonjour à tous, c'est bientôt l'heure du daily !

Pour rendre le point efficace, répondez à ces trois questions en réponse à ce message :

- Qu'est-ce que j'ai fait hier ?
- Qu'est-ce que je fais aujourd'hui ?
- Quels soucis j'anticipe pour ma journée ?

On se retrouve à 9h30 :)
    """

    body = {
        "channel": get_channel_id(),
        "text": daily_message,
        "link_names": True
    }
    response = requests.post("https://slack.com/api/chat.postMessage", json=body, headers=headers)

    return {
        "status": response.status_code,
        "reason": response.text
    }

def get_channel_id():
    return next(
        channel["id"]
        for channel in requests.get("https://slack.com/api/conversations.list", headers=headers).json()["channels"]
        if channel["name"] == os.environ["TEAM_CHANNEL_NAME"]
    )
