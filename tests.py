#!/usr/bin/python
# coding: utf-8
import unittest
from konduto import Konduto
from random import randint

KONDUTO_ID = os.getenv('KONDUTO_ID')
KONDUTO_API_KEY = os.getenv('KONDUTO_API_KEY')


class KondutoTestCase(unittest.TestCase):

    def setUp(self):
        self.konduto = konduto(KONDUTO_API_KEY, KONDUTO_API_KEY)

    def test_check_order(self):
        pass