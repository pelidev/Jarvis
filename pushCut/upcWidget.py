import requests
import os
from combFunctions import openTasks

PUSHCUT_URL = os.getenv('CURRENT_WIDGET_SECRET')

def send_UPC():
    input1 = openTasks.upcomingtasks(0, "_")
    content = "UPC"
    inputs = {}
    payload = {}
    payload["content"] = content

    if input1:
        for i, task in enumerate(input1):
            inputs[f"input{i}"] = task
    else:
        inputs["input0"] = "No tasks scheduled."

    payload["inputs"] = inputs

    print(payload)
    response = requests.post(PUSHCUT_URL, json=payload)
    response.raise_for_status()
    print(response.status_code, response.text)