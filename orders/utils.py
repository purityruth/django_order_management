# utils.py

import africastalking
from decouple import config

def send_sms(recipient, message):
    africastalking.initialize(
        username=config('AFRICASTALKING_USERNAME'),
        api_key=config('AFRICASTALKING_API_KEY'),
    )

    sms = africastalking.SMS
    response = sms.send(message, [recipient], sender_id=config.AFRICASTALKING_SENDER_ID)

    return response
