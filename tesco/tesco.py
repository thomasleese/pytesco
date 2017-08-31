from collections import namedtuple
import re

import requests


class Tesco:

    base_url = 'https://dev.tescolabs.com/{path}'

    def __init__(self, api_key):
        self.api_key = api_key

    def _make_request(self, path, params):
        url = self.base_url.format(path=path)
        headers = {'Ocp-Apim-Subscription-Key': self.api_key}
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def _camelcase_to_snakecase(self, value, do_str=False):
        if isinstance(value, list):
            return [self._camelcase_to_snakecase(x) for x in value]
        elif isinstance(value, dict):
            return {
                self._camelcase_to_snakecase(k, True): self._camelcase_to_snakecase(v)
                for k, v in value.items()
            }
        elif isinstance(value, str) and do_str:
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        else:
            return value

    def _dict_to_object(self, value):
        if isinstance(value, list):
            return [self._dict_to_object(x) for x in value]
        elif isinstance(value, dict):
            return namedtuple('NutritionObject', value.keys())(**{k: self._dict_to_object(v) for k, v in value.items()})
        else:
            return value

    def parse_product(self, data):
        snakecase_data = self._camelcase_to_snakecase(data)
        return self._dict_to_object(snakecase_data)

    def lookup(self, gtin=None, tpnb=None, tpnc=None, catid=None):
        """Lookup a product on Tesco."""

        params = {
            'gtin': gtin,
            'tpnb': tpnb,
            'tpnc': tpnc,
            'catid': catid,
        }

        return [
            self.parse_product(data)
            for data in self._make_request('/product/', params)['products']
        ]
