from decimal import Decimal
from unittest import TestCase

from tesco.data import Nutrition


class TestTesco(TestCase):

    def test_nutrition(self):
        data = {
            "per100Header": "per 100ml",
            "perServingHeader": "150ml",
            "calcNutrients": [
                {
                    "name": "Energy (kJ)",
                    "valuePer100": "182",
                    "valuePerServing": "273"
                },
                {
                    "name": "Energy (kcal)",
                    "valuePer100": "43",
                    "valuePerServing": "65"
                },
                {
                    "name": "Fat (g)",
                    "valuePer100": "0.1",
                    "valuePerServing": "0.1"
                },
                {
                    "name": " of which saturates (g)",
                    "valuePer100": "0.1",
                    "valuePerServing": "0.1"
                },
                {
                    "name": "Carbohydrate (g)",
                    "valuePer100": "8.9",
                    "valuePerServing": "13.4"
                },
                {
                    "name": " of which sugars (g)",
                    "valuePer100": "8.9",
                    "valuePerServing": "13.4"
                },
                {
                    "name": "Fibre (g)",
                    "valuePer100": "0.6",
                    "valuePerServing": "0.9"
                },
                {
                    "name": "Protein (g)",
                    "valuePer100": "0.8",
                    "valuePerServing": "1.2"
                },
                {
                    "name": "Salt (g)",
                    "valuePer100": "0",
                    "valuePerServing": "0"
                },
                {
                    "name": "Vitamin C (mg)",
                    "valuePer100": "33",
                    "valuePerServing": "50"
                },
                {
                    "name": "Folic Acid (\u00b5g)",
                    "valuePer100": "23",
                    "valuePerServing": "35"
                },
                {
                    "name": "Potassium (mg)",
                    "valuePer100": "198",
                    "valuePerServing": "297"
                }
            ]
        }

        nutrition = Nutrition.parse(data)

        assert nutrition.per_100.description == 'per 100ml'
        assert 'Energy' in nutrition.per_100.nutrients
        assert nutrition.per_100.nutrients['Energy'].units == 'kJ'
        assert nutrition.per_100.nutrients['Energy'].value == 182

        assert nutrition.per_serving.description == '150ml'
        assert 'Saturates' in nutrition.per_serving.nutrients
        assert nutrition.per_serving.nutrients['Saturates'].units == 'g'
        assert nutrition.per_serving.nutrients['Saturates'].value == Decimal('0.1')
