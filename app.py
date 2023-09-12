from logging import config
from twilio.rest import Client
import config 



client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to="+17342556699"
    from_="+18556831598"
    body="This is our first message"
)


