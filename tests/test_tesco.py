import os
from unittest import TestCase

from tesco import Tesco


class TestTesco(TestCase):

    api_key = os.environ['TESCO_API_KEY']

    def setUp(self):
        self.tesco = Tesco(self.api_key)

    def test_not_found(self):
        products = self.tesco.lookup(gtin='not real')
        assert len(products) == 0

    def test_one(self):
        products = self.tesco.lookup(gtin='5053990138746')
        assert len(products) == 1

    def test_many(self):
        products = self.tesco.lookup(gtin=['5053990138746', '5053526715960'])
        assert len(products) == 2
