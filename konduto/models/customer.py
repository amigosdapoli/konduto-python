#!/usr/bin/python

class Customer(object):

    __acceptable_keys_list = ["id", "name", "tax_id", "phone1", "phone2",
            "email", "new", "vip", "dob", "created_at", "document_type"]

    def __init__(self, **kwargs):
        [self.__setattr__(key, kwargs.get(key)) for key in self.__acceptable_keys_list]

    def to_json(self):
        return json.loads(self.__dict__)

