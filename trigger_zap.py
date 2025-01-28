import requests
import time
import schedule

# Webhook URL from Zapier
WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/1234567/abcde123/"

# Function to trigger the webhook
def trigger_webhook():
    response = requests.post(WEBHOOK_URL, json={"message": "Zap triggered!"})
    if response.status_code == 200:
        print("Zap triggered successfully.")
    else:
        print(f"Failed to trigger Zap: {response.status_code}, {response.text}")

# Schedule the webhook to run every 9 hours
schedule.every(5).minutes.do(trigger_webhook)

print("Script running...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
