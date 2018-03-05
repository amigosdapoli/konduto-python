#!/usr/bin/python
# coding: utf-8
import unittest
import os
from konduto import Konduto
from random import randint
# Load .env variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


KONDUTO_PUBLIC_KEY = os.getenv('KONDUTO_PUBLIC_KEY')
KONDUTO_PRIVATE_KEY = os.getenv('KONDUTO_PRIVATE_KEY')


class KondutoTestCase(unittest.TestCase):

    def setUp(self):
        self.konduto = Konduto(KONDUTO_PUBLIC_KEY, KONDUTO_PRIVATE_KEY)

    def test_check_order(self):
        response = self.konduto.send_order()
        self.assertEqual(response["status"],"ok")


if __name__ == '__main__':
    unittest.main()
