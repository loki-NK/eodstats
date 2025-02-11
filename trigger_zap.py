import os
import requests

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Function to trigger the webhook
def trigger_webhook():
    if not WEBHOOK_URL:
        print("Error: WEBHOOK_URL is not set.")
        return

    response = requests.post(WEBHOOK_URL, json={"message": "Zap triggered!"})
    
    if response.status_code == 200:
        print("Zap triggered successfully.")
    else:
        print(f"Failed to trigger Zap: {response.status_code}, {response.text}")

# Run the function directly
trigger_webhook()
