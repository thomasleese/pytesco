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

    def lookup(self, gtin=None, tpnb=None, tpnc=None, catid=None):
        params = {
            'gtin': gtin,
            'tpnb': tpnb,
            'tpnc': tpnc,
            'catid': catid,
        }

        return self._make_request('/product/', params)['products']
