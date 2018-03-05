import json
import requests
from base64 import b64encode
import logging

logger = logging.getLogger(__name__)

BASE_URL = "https://api.konduto.com/v1/"

class Konduto(object):
    def __init__(self, api_public_key, api_private_key):
        logger.info("Initializing Konduto Python...")
        self.base_url = BASE_URL
        if len(api_private_key)==21:
        	self.api_private_key = api_private_key
        else:
        	raise Exception("Invalid key! API key length must be of 21")
        self.api_public_key = api_public_key
        self.headers = {
              "Authorization": "Basic {}".format(b64encode(self.api_private_key.encode())),
              "Content-Type": "application/json",
              }

    def send_order(self):
        url = self.base_url + "orders"
        data = {
          "id":"10000000001",
          "visitor":"da39a3ee5e6b4b0d3255bfef95601890afd80709",
          "total_amount":100.00,
          "shipping_amount":20.00,
          "tax_amount":3.45,
          "currency":"USD",
          "installments":2,
          "ip":"170.149.100.10",
          "first_message":"2018-12-20T15:59:01Z",
          "messages_exchanged":30,
          "purchased_at":"2018-12-25T12:00:25Z",
          "analyze": "true",
          "customer":{ },
          "payment":[ ],
          "billing":{ },
          "shipping":{  },
          "shopping_cart":[ ],
          "travel":{ },
          "seller":{ }
        }
        r = requests.post(url, headers=self.headers, json=data)
        print (r.status_code)

        if r.status_code == 444:
        	raise Exception('Error 444 - No Response')

        return r.json()


