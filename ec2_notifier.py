import boto3
import requests
import time

# AWS Configuration
AWS_REGION = "us-east-1"  # Replace with your AWS region
INSTANCE_ID = "i-0dec7ae1549dba4a1"  # Replace with your EC2 instance ID

# Discord Webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1315554436285726740/B0Wb36cKUF8o236R6xljUF_3cSG7VTcKbYAOWocEkQcHgB8zFx6Zvxbq_1zY4P8HZTwI"  # Replace with your Discord webhook URL

# Check interval (in seconds)
CHECK_INTERVAL = 60  # Time between state checks


def get_instance_state(instance_id):
    """Fetch the current state of the EC2 instance."""
    ec2 = boto3.client("ec2", region_name=AWS_REGION)
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response["Reservations"][0]["Instances"][0]["State"]["Name"]
    return state


def send_discord_notification(message):
    """Send a message to the Discord channel."""
    data = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Notification sent to Discord.")
    else:
        print(f"Failed to send notification. Response: {response.status_code}, {response.text}")


def monitor_instance():
    """Monitor the EC2 instance and send notifications on state changes."""
    print(f"Monitoring EC2 instance {INSTANCE_ID} in {AWS_REGION}...")
    last_state = None

    while True:
        try:
            # Get the current state of the instance
            current_state = get_instance_state(INSTANCE_ID)
            print(f"Instance {INSTANCE_ID} state: {current_state}")

            # If the state has changed, notify Discord
            if current_state != last_state:
                if current_state == "running":
                    message = f"🚀 EC2 instance {INSTANCE_ID} is now *running*."
                elif current_state == "stopped":
                    message = f"🛑 EC2 instance {INSTANCE_ID} has been *stopped*."
                elif current_state == "terminated":
                    message = f"⚠️ EC2 instance {INSTANCE_ID} has been *terminated*."
                else:
                    message = f"ℹ️ EC2 instance {INSTANCE_ID} is now in {current_state} state."

                send_discord_notification(message)
                last_state = current_state

            # Wait for the next check
            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    monitor_instance()
