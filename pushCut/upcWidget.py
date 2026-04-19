import requests
import os
from combFunctions import openTasks

PUSHCUT_URL = os.getenv('CURRENT_WIDGET_SECRET')

def send_UPC():
    input1 = openTasks.upcomingtasks(0)
    content = "UPC"
    inputs = {}
    payload = {}
    payload["content"] = content
    for i, task in enumerate(input1):
        inputs[f"input{i}"] = task

    payload["inputs"] = inputs

    print(payload)
    response = requests.post(PUSHCUT_URL, json=payload)
    response.raise_for_status()
    print(response.status_code, response.text)