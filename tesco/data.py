from collections import namedtuple
from decimal import Decimal
import re


Product = namedtuple('Product', [
    'gtin', 'tpnb', 'tpnc', 'description', 'brand', 'qty_contents',
    'product_characteristics', 'ingredients', 'gda', 'nutrition', 'storage',
    'marketing_text', 'pkg_dimensions', 'product_attributes'
])

_Nutrient = namedtuple('_Nutrient', ['name', 'units', 'value'])

class Nutrient(_Nutrient):

    @classmethod
    def _extract_name_and_units(cls, title):
        match = re.match(r'^(?P<name>[\w ]+) \((?P<units>\w+)\)$', title)

        name = match.group('name')

        if name.startswith(' of which '):
            name = name[10:].title()

        units = match.group('units')

        return name, units

    @classmethod
    def parse(cls, data, key):
        name, units = cls._extract_name_and_units(data['name'])
        value = data[f'valuePer{key}']
        return cls(name, units, Decimal(value))

_Serving = namedtuple('_Serving', ['description', 'nutrients'])

class Serving(_Serving):

    @classmethod
    def parse(cls, data, key):
        nutrients = {}

        for record in data['calcNutrients']:
            nutrient = Nutrient.parse(record, key)
            if nutrient.name in nutrients:
                continue
            nutrients[nutrient.name] = nutrient

        return cls(data[f'per{key}Header'], nutrients)


_Nutrition = namedtuple('_Nutrition', ['per_100', 'per_serving'])

class Nutrition(_Nutrition):

    @classmethod
    def parse(cls, data):
        calc_nutrients = data['calcNutrients']

        return cls(
            Serving.parse(data, '100'),
            Serving.parse(data, 'Serving'),
        )
