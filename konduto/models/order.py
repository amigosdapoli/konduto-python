#!/usr/bin/python
import json


class Order(object):

    STATUS_PENDING = "pending"
    STATUS_APPROVED = "approved"
    STATUS_DECLINED = "declined"
    STATUS_FRAUD = "fraud"
    STATUS_NOT_AUTHORIZED = "not_authorized"
    STATUS_CANCELED = "canceled"
    RECOMMENDATION_APPROVE = "approve"
    RECOMMENDATION_DECLINE = "decline"
    RECOMMENDATION_REVIEW = "review"
    RECOMMENDATION_NONE = "none"

    __acceptable_keys_list = ["id", "visitor", "total_amount", "shipping_amount", "tax_amount",
            "currency", "installments", "ip", "customer", "payment", "billing",
            "shipping", "shopping_cart", "travel", "purchased_at", "first_message",
            "messages_exchanged", "seller", "analyze", "recommendation", "score"]

    def __init__(self, **kwargs):
        [self.__setattr__(key, kwargs.get(key)) for key in self.__acceptable_keys_list]

    def to_json(self):
        r = json.dumps(self, 
            default=lambda o: getattr(o, '__dict__', str(o)),
            ensure_ascii=False)
        return json.loads(r)

