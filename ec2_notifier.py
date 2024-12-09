import boto3
import requests
import sys

# AWS Configuration
AWS_REGION = "us-east-1"  # Replace with your AWS region
INSTANCE_ID = "i-0dec7ae1549dba4a1"  # Replace with your EC2 instance ID

# Discord Webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1315554436285726740/B0Wb36cKUF8o236R6xljUF_3cSG7VTcKbYAOWocEkQcHgB8zFx6Zvxbq_1zY4P8HZTwI"  # Replace with your Discord webhook URL


def send_discord_notification(message):
    """Send a message to the Discord channel."""
    try:
        data = {"content": message}
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("Notification sent to Discord.")
        else:
            print(f"Failed to send notification. Response: {response.status_code}, {response.text}")
    except requests.RequestException as e:
        print(f"Error sending Discord notification: {e}")


def manage_instance(action):
    """Start or stop the EC2 instance."""
    ec2 = boto3.client("ec2", region_name=AWS_REGION)
    if action == "start":
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        send_discord_notification(f"🚀 EC2 instance {INSTANCE_ID} has been started.")
    elif action == "stop":
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        send_discord_notification(f"🛑 EC2 instance {INSTANCE_ID} has been stopped.")
    else:
        print("Invalid action. Use 'start' or 'stop'.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python manage_ec2.py <start|stop>")
        sys.exit(1)

    action = sys.argv[1].lower()
    manage_instance(action)
