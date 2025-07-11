import requests
import json
import time

LOG_FILE = "alerts.json"
API_URL = "http://127.0.0.1:8000/api/logs/"

def send_logs():
    with open(LOG_FILE, 'r') as f:
        logs = json.load(f)

    for log in logs:
        response = requests.post(API_URL, json=log)
        print(f"Sent log: {log}")
        print(f"Response: {response.status_code} - {response.text}")
        time.sleep(1)  # simulate real-time flow

if __name__ == "__main__":
    send_logs()
