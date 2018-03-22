#!/usr/bin/python
# coding: utf-8
import unittest
import os
from konduto import Konduto
from konduto.models import Order
from konduto.models import Customer
from konduto.utils import *
from random import randint
# Load .env variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


KONDUTO_PUBLIC_KEY = os.getenv('KONDUTO_PUBLIC_KEY')
KONDUTO_PRIVATE_KEY = os.getenv('KONDUTO_PRIVATE_KEY')


class KondutoTestCase(unittest.TestCase):

    unique_id = None

    def setUp(self):
        self.konduto = Konduto(KONDUTO_PUBLIC_KEY, KONDUTO_PRIVATE_KEY)

    def _build_simple_customer(self, info=None):
        return Customer(**{
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

    def _build_simple_order(self, info=None):
        self.unique_id = str(randint(1, 100000))
        customer = self._build_simple_customer()
        order_json = {
            "id": self.unique_id,
            "visitor": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
            "total_amount": 100.01,  # Result approve in test env
            "shipping_amount": 20.00,
            "tax_amount": 3.45,
            "currency": "BRL",
            "installments": 2,
            "ip": "189.68.156.100",
            "customer": customer
            }

        if info is not None:
            order_json.update(info)

        order = Order(**order_json)

        return order

    def _assert_order1_fields(self, order):
        self.assertEqual(self.unique_id, order.id)
        self.assertEqual("da39a3ee5e6b4b0d3255bfef95601890afd80709", order.visitor)
        self.assertEqual(100.01, order.total_amount)
        self.assertEqual(20.0, order.shipping_amount)
        self.assertEqual(3.45, order.tax_amount)
        self.assertEqual("BRL", order.currency)
        self.assertEqual(2, order.installments)
        self.assertEqual("189.68.156.100", order.ip)
        self.assertIsInstance(order.customer, Customer)
        customer = order.customer
        self.assertEqual("28372", customer.id)
        self.assertEqual("Júlia da Silva", customer.name)
        self.assertEqual("12345678909", customer.tax_id)
        #self.assertDate("1970-12-25", customer.getDob())
        self.assertEqual("11-1234-5678", customer.phone1)
        self.assertEqual("21-2143-6578", customer.phone2)
        self.assertEqual("jsilva@exemplo.com.br", customer.email)
        #self.assertDate("2010-12-25", customer.getCreatedAt())
        self.assertFalse(customer.new)
        self.assertFalse(customer.vip)
        #self.assertOrderResponse(order, "APPROVE", 0.01)
    
    def test_expect_recommendation_approve(self):
        order = self._build_simple_order()
        response = self.konduto.analyze(order)
        self.assertEqual(response.recommendation, RECCOMENDATION_APPROVE)

    def test_expect_recommendation_review(self):
        order = self._build_simple_order({"total_amount": 100.31})
        response = self.konduto.analyze(order)
        self.assertEqual(response.recommendation, RECCOMENDATION_REVIEW)
    
    def test_expect_recommendation_decline(self):
        order = self._build_simple_order({"total_amount": 100.61})
        response = self.konduto.analyze(order)
        self.assertEqual(response.recommendation, RECCOMENDATION_DECLINE)

    def test_assert_all_fields(self):
        order = self._build_simple_order()
        order = self.konduto.analyze(order)
        self._assert_order1_fields(order)


if __name__ == '__main__':
    unittest.main()
