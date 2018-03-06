import json
import requests
from base64 import b64encode
import logging
from random import randint

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

    def analyze(self, order=None):
        url = self.base_url + "orders"

        unique_id = randint(1, 100000)
        data = {
            "id": str(unique_id),
            "visitor": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
            "total_amount": 100.01,  # Result approve in test env
            "shipping_amount": 20.00,
            "tax_amount": 3.45,
            "currency": "BRL",
            "installments": 2,
            "ip": "189.68.156.100",
            "customer": {
                "id": "28372",
                "name": "Júlia da Silva",
                "tax_id": "12345678909",
                "dob": "1970-12-25",
                "phone1": "11-1234-5678",
                "phone2": "21-2143-6578",
                "email": "jsilva@exemplo.com.br",
                "created_at": "2010-12-25",
                "new": False,
                "vip": False}
            }
        r = requests.post(url, headers=self.headers, json=data)
        logger.debug(r.status_code)
        logger.debug(dir(r.request))
        logger.debug(r.request.body)
        logger.debug(dir(r))

        if r.status_code != 200:
        	r.raise_for_status()
        
        logger.debug(r.json())
        return r.json()


