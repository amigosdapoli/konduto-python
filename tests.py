#!/usr/bin/python
# coding: utf-8
import unittest
import os
from konduto import Konduto
from konduto.models import Order
from konduto.models import Customer
from random import randint
# Load .env variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


KONDUTO_PUBLIC_KEY = os.getenv('KONDUTO_PUBLIC_KEY')
KONDUTO_PRIVATE_KEY = os.getenv('KONDUTO_PRIVATE_KEY')


class KondutoTestCase(unittest.TestCase):

    def setUp(self):
        self.konduto = Konduto(KONDUTO_PUBLIC_KEY, KONDUTO_PRIVATE_KEY)

    def _build_simple_order(self, info={}):
        unique_id = randint(1, 100000)
        order_json = {
            "id": str(unique_id),
            "visitor": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
            "total_amount": 100.01,  # Result approve in test env
            "shipping_amount": 20.00,
            "tax_amount": 3.45,
            "currency": "BRL",
            "installments": 2,
            "ip": "189.68.156.100",
            "customer": Customer(**{
                "id": "28372",
                "name": "Júlia da Silva",
                "tax_id": "12345678909",
                "dob": "1970-12-25",
                "phone1": "11-1234-5678",
                "phone2": "21-2143-6578",
                "email": "jsilva@exemplo.com.br",
                "created_at": "2010-12-25",
                "new": False,
                "vip": False})
            }
        order = Order(**order_json)

        return order

    def test_expect_recommendation_approve(self):
        order = self._build_simple_order()
        response = self.konduto.analyze(order)

        self.assertEqual(response['order']['recommendation'],'APPROVE')


if __name__ == '__main__':
    unittest.main()
