import requests
import time
import schedule

# Webhook URL from Zapier
WEBHOOK_URL = "https://webhook.site/599094f8-8b8e-482b-8a85-87da43fca73e"

# Function to trigger the webhook
def trigger_webhook():
    response = requests.post(WEBHOOK_URL, json={"message": "Zap triggered!"})
    if response.status_code == 200:
        print("Zap triggered successfully.")
    else:
        print(f"Failed to trigger Zap: {response.status_code}, {response.text}")

# Schedule the webhook to run every 9 hours
schedule.every(1).minutes.do(trigger_webhook)

print("Script running...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
