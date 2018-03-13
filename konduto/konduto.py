import json
import requests
from base64 import b64encode
import logging
from random import randint
from konduto.models import Order, Customer

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
        api_public_key64 = b64encode(self.api_private_key.encode())
        self.headers = {
              "Authorization": "Basic {}".format(api_public_key64.decode()),
              "Content-Type": "application/json",
              }

    def analyze(self, order):
        url = self.base_url + "orders"
        data = order.to_json()        
        r = requests.post(url, headers=self.headers, json=data)

        if r.status_code != 200:
        	r.raise_for_status()
        
        data.update({"customer": Customer(**data['customer'])})
        new_order = Order(**{**data, **r.json()['order']})
        return new_order


