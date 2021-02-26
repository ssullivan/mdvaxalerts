import requests
import os
from base64 import b64decode
from urllib.parse import urlencode
from twilio.rest import Client
import datetime
from dateutil.parser import parse
from datetime import timedelta
from os import environ

def decrypt(encoded:str) -> str:
  return encoded

def get_setting(setting:str) -> str:
  if environ.get(setting) is not None:
    return environ.get(setting)
  else:
    return ""

TWILIO_ACCONT = decrypt(get_setting('TWILIO_ACCOUNT'))
TWILIO_TOKEN = decrypt(get_setting('TWILIO_TOKEN'))
ALERT_PHONE = decrypt(get_setting('ALERT_PHONE'))
TWILIO_PHONE = decrypt(get_setting('TWILIO_PHONE'))

def sms_alert(message: str, from_phone: str = TWILIO_PHONE, to_phone: str = None):
  client = Client(
      TWILIO_ACCONT,
      TWILIO_TOKEN,
  )

  message = client.messages.create(
      body=message,
      from_=from_phone,
      to=to_phone
  )

  return message


response = requests.post("https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability",
                         json={"serviceId":"99","position":{"latitude":39.2590567,"longitude":-76.8951551},"appointmentAvailability":{"startDateTime":str(datetime.date.today() + datetime.timedelta(days=1))},"radius":25})

result = response.json()
if result is not None:
  if result['appointmentsAvailable']:
    sms_alert("Walgreens Has Appointments Available", TWILIO_PHONE, ALERT_PHONE)
  else:
    print("No appointments available")
j = 0