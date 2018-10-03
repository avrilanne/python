import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv
from twilio.rest import Client

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
MY_NUMBER = os.getenv("MY_NUMBER")
TARGET_NUMBER = os.getenv("TARGET_NUMBER")


api_instance = giphy_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
s = 'programmer' # str | Search term.

try:
    api_response = api_instance.gifs_translate_get(api_key, s)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_translate_get: %s\n" % e)


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

beginning = 'https://media.giphy.com/media/'
gif_id = api_response.data.id
end = '/giphy.gif'

destination_url = '%s%s%s'%(beginning, gif_id, end)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_=MY_NUMBER,
    media_url=destination_url,
    to=TARGET_NUMBER
)

print(message.sid)
