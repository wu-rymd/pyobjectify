import pyobjectify as pyob

from pandas import DataFrame
import os
import unittest

DIR = os.path.dirname(__file__) or "."

URL = f"{DIR}/data/example.json"


class TestPyobjectify(unittest.TestCase):
    def test_connectivity_resource(self):
        connectivity = pyob.url_to_connectivity(URL)
        actual = pyob.retrieve_resource(URL, connectivity)
        expected = pyob.Resource(URL, pyob.Connectivity.LOCAL)
        self.assertEqual(actual, expected)

    def test_connectivity_resource_types(self):
        connectivity = pyob.url_to_connectivity(URL)
        resource = pyob.retrieve_resource(URL, connectivity)
        actual = pyob.get_resource_types(resource)
        assert pyob.InputType.JSON in actual

    def test_connectivity_resource_types_conversion(self):
        connectivity = pyob.url_to_connectivity(URL)
        resource = pyob.retrieve_resource(URL, connectivity)
        resource_types = pyob.get_resource_types(resource)
        actual = pyob.get_conversions(resource_types)
        expected = [(pyob.InputType.JSON, dict), (pyob.InputType.JSON, list), (pyob.InputType.JSON, DataFrame)]
        self.assertEqual(actual, expected)

    def test_connectivity_resource_types_conversion_output(self):
        connectivity = pyob.url_to_connectivity(URL)
        resource = pyob.retrieve_resource(URL, connectivity)
        resource_types = pyob.get_resource_types(resource)
        conversions = pyob.get_conversions(resource_types)
        actual = pyob.convert(resource, conversions)
        expected = {
            "quiz": {
                "q1": {
                    "question": "Question 1",
                    "options": ["Choice A", "Choice B", "Choice C", "Choice D"],
                    "answer": "Choice C",
                },
                "q2": {"question": "Question 2", "options": ["A", "B", "C", "D"], "answer": "C"},
            }
        }
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
