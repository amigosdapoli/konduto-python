#!/usr/bin/python
# coding: utf-8
import unittest
import os
from konduto import Konduto
from konduto.models import Order
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
        order = Order()
        return order

    def test_expect_recommendation_approve(self):
        order = self._build_simple_order()
        response = self.konduto.analyze(order)

        self.assertEqual(response['order']['recommendation'],'APPROVE')


if __name__ == '__main__':
    unittest.main()
