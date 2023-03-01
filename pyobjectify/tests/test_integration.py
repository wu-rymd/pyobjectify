import pyobjectify

import os
import json
import unittest

DIR = os.path.dirname(__file__) or "."


class TestPyobjectify(unittest.TestCase):
    def test_json_api_to_json_file_to_dict(self):
        json_dict = pyobjectify.json_api_to_dict("https://api.rymd.app/data")
        with open(f"{DIR}/data/test.json", "w") as f:
            json.dump(json_dict, f)

        json_file = open(f"{DIR}/data/test.json", "r")
        actual = pyobjectify.json_file_to_dict(json_file)
        expected = [
            {
                "condition": "Clear sky",
                "feels_like": 25,
                "humidity": 85,
                "icon": "https://openweathermap.org/img/wn/01n@2x.png",
                "name": "Manhattan",
                "temp_max": 37,
                "temp_min": 24,
                "wind_speed": 9,
            },
            {
                "condition": "Clear sky",
                "feels_like": 26,
                "humidity": 83,
                "icon": "https://openweathermap.org/img/wn/01n@2x.png",
                "name": "Brooklyn",
                "temp_max": 38,
                "temp_min": 25,
                "wind_speed": 9,
            },
            {
                "condition": "Snow",
                "feels_like": 25,
                "humidity": 78,
                "icon": "https://openweathermap.org/img/wn/13n@2x.png",
                "name": "Queens",
                "temp_max": 38,
                "temp_min": 25,
                "wind_speed": 9,
            },
            {
                "condition": "Few clouds",
                "feels_like": 24,
                "humidity": 81,
                "icon": "https://openweathermap.org/img/wn/02n@2x.png",
                "name": "The Bronx",
                "temp_max": 38,
                "temp_min": 24,
                "wind_speed": 9,
            },
            {
                "condition": "Clear sky",
                "feels_like": 25,
                "humidity": 85,
                "icon": "https://openweathermap.org/img/wn/01n@2x.png",
                "name": "Staten Island",
                "temp_max": 38,
                "temp_min": 24,
                "wind_speed": 9,
            },
        ]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
