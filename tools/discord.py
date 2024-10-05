
import os
import requests
from datetime import datetime
from pydantic import BaseModel, Field


class Tools:
    class Valves(BaseModel):
        WEBHOOK_URL: str = Field(
            default="",
            description="The URL of the Discord webhook to send messages to.",
        )

    def __init__(self):
        self.valves = self.Valves()
        pass

    def send_message(self, message_content: str) -> str:
        """
        Send a message to a specified Discord channel using a webhook.

        :param message_content: The content of the message to be sent to the Discord channel.
        :return: None
        """

        # Check if the webhook URL has been set
        if not self.valves.WEBHOOK_URL:
            return "Let the user know webhook URL was not provided. Please configure the webhook URL."

        data = {"content": f"{message_content} - Sent from Open WebUI"}

        response = requests.post(self.valves.WEBHOOK_URL, json=data)

        if response.status_code == 204:
            return "Message successfully sent, Let the user know the message has been sent."
        else:
            return f"Failed to send message. HTTP Status Code: {response.status_code},  Let the user know there were some issues."
