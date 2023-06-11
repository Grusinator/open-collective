import datetime
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from ics import Calendar
import requests


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    # Fetch the iCal data
    ic_url = "https://your_ical_link.ics"
    c = Calendar(requests.get(ic_url).text)

    # Check if there's an event today
    today = datetime.date.today()
    for event in c.events:
        if event.begin.date() == today:
            # Send a message to the Slack channel
            send_message_to_slack(event.name)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

def send_message_to_slack(event_name: str):
    client = WebClient(token=os.environ['SLACK_API_TOKEN'])
    channel_id = "C1234567"  # Replace with your channel ID

    try:
        # Call the chat.postMessage method using the WebClient
        result = client.chat_postMessage(
            channel=channel_id,
            text=f"Reminder: The event '{event_name}' is happening today!")
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        logging.error(f"Got an error: {e.response['error']}")
