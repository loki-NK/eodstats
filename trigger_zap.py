import requests

# Webhook URL from Zapier
WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/11394097/2fik0fg/"

# Function to trigger the webhook
def trigger_webhook():
    response = requests.post(WEBHOOK_URL, json={"message": "Zap triggered!"})
    if response.status_code == 200:
        print("Zap triggered successfully.")
    else:
        print(f"Failed to trigger Zap: {response.status_code}, {response.text}")

# Run the function directly
trigger_webhook()
