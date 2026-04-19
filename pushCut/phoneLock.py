import requests
import os

PUSHCUT_URL = os.getenv('NOTIFICATION_SECRET')

def timer_Push(message, delay):
    title = "Jarvis Notification"
    text = message if message else "Whatever it was...it's done now."


    payload = {}
    payload['title'] = title
    payload['text'] = text
    while True:
        if delay:
            payload['delay'] = delay
            break
        else:
            break

    response = requests.post(PUSHCUT_URL, json=payload)
    print("Notification sent!")
    print(response.status_code, response.text)
    response.raise_for_status()
