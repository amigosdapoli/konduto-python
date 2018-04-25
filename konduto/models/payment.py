#!/usr/bin/python
import json


class Payment(object):
    """
    Implemented only for one payment
    """

    TYPE_CREDIT = "credit"
    TYPE_BOLETO = "boleto"
    TYPE_DEBIT = "debit"
    TYPE_TRANSFER = "transfer"
    TYPE_VOUCHER = "voucher"

    STATUS_APPROVED = "approved"
    STATUS_DECLINED = "declined"
    STATUS_PENDING  = "pending"

    __acceptable_keys_list = ["type", "bin", "last4", "expiration_date", "status"]

    def __init__(self, **kwargs):
        [self.__setattr__(key, kwargs.get(key)) for key in self.__acceptable_keys_list]

    def to_json(self):
        r = json.dumps(self, 
            default=lambda o: getattr(o, '__dict__', str(o)),
            ensure_ascii=False)
        return json.loads(r)