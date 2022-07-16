import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import os



URL_OF_INTEREST = "https://articulo.mercadolibre.com.mx/MLM-962772639-carcasa-cargador-de-6000mah-para-samsung-galaxy-s10-_JM#position=1&search_layout=stack&type=pad&tracking_id=93286187-387a-4d74-b7b2-0991e97b4168#position=1&search_layout=stack&type=pad&tracking_id=93286187-387a-4d74-b7b2-0991e97b4168&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=NjZkNDc2ODktYTRhZi00OTI2LTg1MzgtNWYxM2M3YWY4ZTA2"
TARGET_PRICE = 800.00
TWILIO_VIRTUAL_NUMBER = "+19402896137"
TWILIO_VERIFIED_NUMBER = "+525546476943"

response = requests.get(URL_OF_INTEREST)
soup = BeautifulSoup(response.text, 'html.parser')
price = str(soup.find(name="meta", itemprop="price"))
price = price.split('"')

if float(price[1]) < TARGET_PRICE:
    client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_AUTH_TOKEN"])
    message = client.messages.create(
        body=f"This is your lucky day. The item you were looking it's only {price[1]} MXN, bellow your target price.",
        from_=TWILIO_VIRTUAL_NUMBER,
        to=TWILIO_VERIFIED_NUMBER
    )
    print(message.sid)
