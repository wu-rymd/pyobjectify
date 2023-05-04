import pyobjectify as pyob

from pandas import DataFrame, json_normalize
import os
import unittest

DIR = os.path.dirname(__file__) or "."

URL_LOCAL = f"{DIR}/data/example.json"
URL_ONLINE_STATIC = "https://bit.ly/42KCUSv"

URL_JSON = f"{DIR}/data/example.json"
URL_CSV = f"{DIR}/data/example.csv"
URL_TSV = f"{DIR}/data/example.tsv"
URL_XML = f"{DIR}/data/example.xml"
URL_XLSX = f"{DIR}/data/example.xlsx"
URL_OTHER = f"{DIR}/data/data.example"

CONNECTIVITY_UNSUPPORTED = str
OUTPUT_TYPE_UNSUPPORTED = str


class TestPyobjectify(unittest.TestCase):
    def test_url_to_connectivity_local(self):
        actual = pyob.url_to_connectivity(URL_LOCAL)
        expected = pyob.Connectivity.LOCAL
        self.assertEqual(actual, expected)

    def test_url_to_connectivity_online_static(self):
        actual = pyob.url_to_connectivity(URL_ONLINE_STATIC)
        expected = pyob.Connectivity.ONLINE_STATIC
        self.assertEqual(actual, expected)

    def test_retrieve_resource_local(self):
        actual = pyob.retrieve_resource(URL_LOCAL, pyob.Connectivity.LOCAL)
        expected = pyob.Resource(URL_LOCAL, pyob.Connectivity.LOCAL)
        self.assertEqual(actual, expected)

    def test_retrieve_resource_online_static(self):
        actual = pyob.retrieve_resource(URL_ONLINE_STATIC, pyob.Connectivity.ONLINE_STATIC)
        expected = pyob.Resource(URL_ONLINE_STATIC, pyob.Connectivity.ONLINE_STATIC)
        self.assertEqual(actual, expected)

    def test_retrieve_resource_online_error(self):
        with self.assertRaises(TypeError):
            pyob.retrieve_resource(URL_ONLINE_STATIC, CONNECTIVITY_UNSUPPORTED)

    def test_get_resource_types_json(self):
        resource = pyob.Resource(URL_JSON, pyob.Connectivity.LOCAL)
        actual = pyob.get_resource_types(resource)
        assert pyob.InputType.JSON in actual

    def test_get_resource_types_csv(self):
        resource = pyob.Resource(URL_CSV, pyob.Connectivity.LOCAL)
        actual = pyob.get_resource_types(resource)
        assert pyob.InputType.CSV in actual

    def test_get_resource_types_tsv(self):
        resource = pyob.Resource(URL_TSV, pyob.Connectivity.LOCAL)
        actual = pyob.get_resource_types(resource)
        assert pyob.InputType.TSV in actual

    def test_get_resource_types_xml(self):
        resource = pyob.Resource(URL_XML, pyob.Connectivity.LOCAL)
        actual = pyob.get_resource_types(resource)
        assert pyob.InputType.XML in actual

    def test_get_resource_types_xlsx(self):
        resource = pyob.Resource(URL_XLSX, pyob.Connectivity.LOCAL)
        actual = pyob.get_resource_types(resource)
        assert pyob.InputType.XLSX in actual

    def test_get_resource_types_error(self):
        resource = pyob.Resource(URL_OTHER, pyob.Connectivity.LOCAL)
        with self.assertRaises(TypeError):
            pyob.get_resource_types(resource)

    def test_get_conversions_json(self):
        actual = pyob.get_conversions([pyob.InputType.JSON])
        expected = [(pyob.InputType.JSON, dict), (pyob.InputType.JSON, list), (pyob.InputType.JSON, DataFrame)]
        self.assertEqual(actual, expected)

    def test_get_conversions_csv(self):
        actual = pyob.get_conversions([pyob.InputType.CSV])
        expected = [(pyob.InputType.CSV, list)]
        self.assertEqual(actual, expected)

    def test_get_conversions_tsv(self):
        actual = pyob.get_conversions([pyob.InputType.TSV])
        expected = [(pyob.InputType.TSV, list)]
        self.assertEqual(actual, expected)

    def test_get_conversions_xml(self):
        actual = pyob.get_conversions([pyob.InputType.XML])
        expected = [(pyob.InputType.XML, dict)]
        self.assertEqual(actual, expected)

    def test_get_conversions_xlsx(self):
        actual = pyob.get_conversions([pyob.InputType.XLSX])
        expected = [(pyob.InputType.XLSX, dict)]
        self.assertEqual(actual, expected)

    def test_get_conversions_json_dataframe(self):
        actual = pyob.get_conversions([pyob.InputType.JSON], DataFrame)
        expected = [(pyob.InputType.JSON, DataFrame)]
        self.assertEqual(actual, expected)

    def test_get_conversions_error(self):
        with self.assertRaises(TypeError):
            pyob.get_conversions([pyob.InputType.JSON], OUTPUT_TYPE_UNSUPPORTED)

    def test_convert_json_dict(self):
        resource = pyob.Resource(URL_JSON, pyob.Connectivity.LOCAL)
        actual = pyob.convert(resource, [(pyob.InputType.JSON, dict)])
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

    def test_convert_json_other_dict(self):
        resource = pyob.Resource(URL_JSON, pyob.Connectivity.LOCAL)
        actual = pyob.convert(resource, [(pyob.InputType.JSON, OUTPUT_TYPE_UNSUPPORTED), (pyob.InputType.JSON, dict)])
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

    def test_convert_json_list(self):
        resource = pyob.Resource(URL_JSON, pyob.Connectivity.LOCAL)
        actual = pyob.convert(resource, [(pyob.InputType.JSON, list)])
        expected = [
            {
                "quiz": {
                    "q1": {
                        "question": "Question 1",
                        "options": ["Choice A", "Choice B", "Choice C", "Choice D"],
                        "answer": "Choice C",
                    },
                    "q2": {"question": "Question 2", "options": ["A", "B", "C", "D"], "answer": "C"},
                }
            }
        ]
        self.assertEqual(actual, expected)

    def test_convert_json_dataframe(self):
        resource = pyob.Resource(URL_JSON, pyob.Connectivity.LOCAL)
        actual = pyob.convert(resource, [(pyob.InputType.JSON, DataFrame)])
        json = {
            "quiz": {
                "q1": {
                    "question": "Question 1",
                    "options": ["Choice A", "Choice B", "Choice C", "Choice D"],
                    "answer": "Choice C",
                },
                "q2": {"question": "Question 2", "options": ["A", "B", "C", "D"], "answer": "C"},
            }
        }
        expected = json_normalize(json)
        assert DataFrame.compare(actual, expected).empty

    def test_convert_csv_list(self):
        resource = pyob.Resource(URL_CSV, pyob.Connectivity.LOCAL)
        actual = pyob.convert(resource, [(pyob.InputType.CSV, list)])
        expected = [
            {
                "Borough": "Bronx",
                "Postcode": "10458",
                "Phone": "718-935-2178",
                "Districts Served": "7, 9, 10",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "1 Fordham Plaza",
                "Latitude": "40.860994",
                "Longitude": "-73.890073",
                "Community Board": "6",
                "Council District": "15",
                "Census Tract": "387",
                "BIN": "",
                "BBL": "",
                "NTA": "Belmont                                                                    ",
                "Location 1": "(40.860994, -73.890073)",
            },
            {
                "Borough": "Brooklyn",
                "Postcode": "11230",
                "Phone": "718-935-2313",
                "Districts Served": "17, 18, 22",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "1780 Ocean Avenue\n",
                "Latitude": "40.618915",
                "Longitude": "-73.955115",
                "Community Board": "14",
                "Council District": "48",
                "Census Tract": "538",
                "BIN": "3180747",
                "BBL": "3067390077",
                "NTA": "Midwood                                                                    ",
                "Location 1": "(40.618915, -73.955115)",
            },
            {
                "Borough": "Brooklyn (Note: General Education Only)",
                "Postcode": "11217",
                "Phone": "718-935-2371",
                "Districts Served": "13, 14, 15, 16",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "29 Fort Greene Place\n(Note: General Education Only)",
                "Latitude": "40.688834",
                "Longitude": "-73.976905",
                "Community Board": "2",
                "Council District": "35",
                "Census Tract": "33",
                "BIN": "3058752",
                "BBL": "3020980013",
                "NTA": "Fort Greene                                                                ",
                "Location 1": "(40.688834, -73.976905)",
            },
            {
                "Borough": "Brooklyn (Note: Special Education Only)",
                "Postcode": "11201",
                "Phone": "718-935-4908",
                "Districts Served": "13, 14, 15, 16",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "131 Livingston Street\n(Note: Special Education Only)",
                "Latitude": "40.690743",
                "Longitude": "-73.988605",
                "Community Board": "2",
                "Council District": "33",
                "Census Tract": "37",
                "BIN": "3000420",
                "BBL": "3001540001",
                "NTA": "DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum Hill                           ",
                "Location 1": "(40.690743, -73.988605)",
            },
            {
                "Borough": "Brooklyn",
                "Postcode": "11209",
                "Phone": "718-935-2331",
                "Districts Served": "20, 21",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "415 89th Street\n",
                "Latitude": "40.619931",
                "Longitude": "-74.028086",
                "Community Board": "10",
                "Council District": "43",
                "Census Tract": "160",
                "BIN": "3154215",
                "BBL": "3060650043",
                "NTA": "Bay Ridge                                                                  ",
                "Location 1": "(40.619931, -74.028086)",
            },
            {
                "Borough": "Brooklyn",
                "Postcode": "11233",
                "Phone": "718-935-2340",
                "Districts Served": "19, 23, 32",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "1665 St Mark's Avenue\n",
                "Latitude": "40.673138",
                "Longitude": "-73.912024",
                "Community Board": "16",
                "Council District": "41",
                "Census Tract": "36501",
                "BIN": "3039123",
                "BBL": "3014540054",
                "NTA": "Ocean Hill                                                                 ",
                "Location 1": "(40.673138, -73.912024)",
            },
            {
                "Borough": "Bronx",
                "Postcode": "10462",
                "Phone": "718-935-2278",
                "Districts Served": "8, 11, 12",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "1230 Zerega Avenue\n ",
                "Latitude": "40.833586",
                "Longitude": "-73.845099",
                "Community Board": "9",
                "Council District": "13",
                "Census Tract": "96",
                "BIN": "2027195",
                "BBL": "2038420002",
                "NTA": "Westchester-Unionport                                                      ",
                "Location 1": "(40.833586, -73.845099)",
            },
            {
                "Borough": "Manhattan",
                "Postcode": "10001",
                "Phone": "718-935-2383",
                "Districts Served": "1, 2, 4",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "333 Seventh Avenue\n",
                "Latitude": "40.747629",
                "Longitude": "-73.99306",
                "Community Board": "5",
                "Council District": "3",
                "Census Tract": "95",
                "BIN": "1015097",
                "BBL": "1008040001",
                "NTA": "Midtown-Midtown South                                                      ",
                "Location 1": "(40.747629, -73.99306)",
            },
            {
                "Borough": "Staten Island",
                "Postcode": "10301",
                "Phone": "718-935-2402",
                "Districts Served": "31",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "718 Ocean Terrace",
                "Latitude": "40.608405",
                "Longitude": "-74.101919",
                "Community Board": "2",
                "Council District": "50",
                "Census Tract": "177",
                "BIN": "1015097",
                "BBL": "1008040001",
                "NTA": "Todt Hill-Emerson Hill-Heartland Village-Lighthouse Hill                   ",
                "Location 1": "(40.608405, -74.101919)",
            },
            {
                "Borough": "Queens",
                "Postcode": "11354",
                "Phone": "718-935-2391",
                "Districts Served": "25, 26",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "30 48 Linden Place",
                "Latitude": "40.770185",
                "Longitude": "-73.832925",
                "Community Board": "7",
                "Council District": "20",
                "Census Tract": "869",
                "BIN": "4100749",
                "BBL": "4043700050",
                "NTA": "Flushing                                                                   ",
                "Location 1": "(40.770185, -73.832925)",
            },
            {
                "Borough": "Queens",
                "Postcode": "11435",
                "Phone": "718-935-2393",
                "Districts Served": "27, 28, 29",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "90 27 Sutphin Boulevard",
                "Latitude": "40.70234",
                "Longitude": "-73.808148",
                "Community Board": "12",
                "Council District": "24",
                "Census Tract": "240",
                "BIN": "4206784",
                "BBL": "4096770007",
                "NTA": "Jamaica                                                                    ",
                "Location 1": "(40.70234, -73.808148)",
            },
            {
                "Borough": "Queens",
                "Postcode": "11101",
                "Phone": "718-935-2386",
                "Districts Served": "24, 30",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "28 11 Queens Plaza",
                "Latitude": "40.75008",
                "Longitude": "-73.938208",
                "Community Board": "1",
                "Council District": "26",
                "Census Tract": "33",
                "BIN": "4005022",
                "BBL": "4004170002",
                "NTA": "Queensbridge-Ravenswood-Long Island City                                   ",
                "Location 1": "(40.75008, -73.938208)",
            },
            {
                "Borough": "Manhattan",
                "Postcode": "10027",
                "Phone": "718-935-2385",
                "Districts Served": "3, 5, 6",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "388 125th Street\n",
                "Latitude": "40.747629",
                "Longitude": "-73.99306",
                "Community Board": "5",
                "Council District": "3",
                "Census Tract": "95",
                "BIN": "",
                "BBL": "",
                "NTA": "",
                "Location 1": "(40.747629, -73.99306)",
            },
        ]
        self.assertEqual(actual, expected)

    def test_convert_tsv_list(self):
        resource = pyob.Resource(URL_TSV, pyob.Connectivity.LOCAL)
        actual = pyob.convert(resource, [(pyob.InputType.TSV, list)])
        expected = [
            {
                "\ufeffBorough": "Bronx",
                "Postcode": "10458",
                "Phone": "718-935-2178",
                "Districts Served": "7, 9, 10",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "1 Fordham Plaza",
                "Latitude": "40.860994",
                "Longitude": "-73.890073",
                "Community Board": "6",
                "Council District": "15",
                "Census Tract": "387",
                "BIN": "",
                "BBL": "",
                "NTA": "Belmont                                                                    ",
                "Location 1": "(40.860994, -73.890073)",
            },
            {
                "\ufeffBorough": "Brooklyn",
                "Postcode": "11230",
                "Phone": "718-935-2313",
                "Districts Served": "17, 18, 22",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "1780 Ocean Avenue\n",
                "Latitude": "40.618915",
                "Longitude": "-73.955115",
                "Community Board": "14",
                "Council District": "48",
                "Census Tract": "538",
                "BIN": "3180747",
                "BBL": "3067390077",
                "NTA": "Midwood                                                                    ",
                "Location 1": "(40.618915, -73.955115)",
            },
            {
                "\ufeffBorough": "Brooklyn (Note: General Education Only)",
                "Postcode": "11217",
                "Phone": "718-935-2371",
                "Districts Served": "13, 14, 15, 16",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "29 Fort Greene Place\n(Note: General Education Only)",
                "Latitude": "40.688834",
                "Longitude": "-73.976905",
                "Community Board": "2",
                "Council District": "35",
                "Census Tract": "33",
                "BIN": "3058752",
                "BBL": "3020980013",
                "NTA": "Fort Greene                                                                ",
                "Location 1": "(40.688834, -73.976905)",
            },
            {
                "\ufeffBorough": "Brooklyn (Note: Special Education Only)",
                "Postcode": "11201",
                "Phone": "718-935-4908",
                "Districts Served": "13, 14, 15, 16",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "131 Livingston Street\n(Note: Special Education Only)",
                "Latitude": "40.690743",
                "Longitude": "-73.988605",
                "Community Board": "2",
                "Council District": "33",
                "Census Tract": "37",
                "BIN": "3000420",
                "BBL": "3001540001",
                "NTA": "DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum Hill                           ",
                "Location 1": "(40.690743, -73.988605)",
            },
            {
                "\ufeffBorough": "Brooklyn",
                "Postcode": "11209",
                "Phone": "718-935-2331",
                "Districts Served": "20, 21",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "415 89th Street\n",
                "Latitude": "40.619931",
                "Longitude": "-74.028086",
                "Community Board": "10",
                "Council District": "43",
                "Census Tract": "160",
                "BIN": "3154215",
                "BBL": "3060650043",
                "NTA": "Bay Ridge                                                                  ",
                "Location 1": "(40.619931, -74.028086)",
            },
            {
                "\ufeffBorough": "Brooklyn",
                "Postcode": "11233",
                "Phone": "718-935-2340",
                "Districts Served": "19, 23, 32",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "1665 St Mark's Avenue\n",
                "Latitude": "40.673138",
                "Longitude": "-73.912024",
                "Community Board": "16",
                "Council District": "41",
                "Census Tract": "36501",
                "BIN": "3039123",
                "BBL": "3014540054",
                "NTA": "Ocean Hill                                                                 ",
                "Location 1": "(40.673138, -73.912024)",
            },
            {
                "\ufeffBorough": "Bronx",
                "Postcode": "10462",
                "Phone": "718-935-2278",
                "Districts Served": "8, 11, 12",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "1230 Zerega Avenue\n ",
                "Latitude": "40.833586",
                "Longitude": "-73.845099",
                "Community Board": "9",
                "Council District": "13",
                "Census Tract": "96",
                "BIN": "2027195",
                "BBL": "2038420002",
                "NTA": "Westchester-Unionport                                                      ",
                "Location 1": "(40.833586, -73.845099)",
            },
            {
                "\ufeffBorough": "Manhattan",
                "Postcode": "10001",
                "Phone": "718-935-2383",
                "Districts Served": "1, 2, 4",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "333 Seventh Avenue\n",
                "Latitude": "40.747629",
                "Longitude": "-73.99306",
                "Community Board": "5",
                "Council District": "3",
                "Census Tract": "95",
                "BIN": "1015097",
                "BBL": "1008040001",
                "NTA": "Midtown-Midtown South                                                      ",
                "Location 1": "(40.747629, -73.99306)",
            },
            {
                "\ufeffBorough": "Staten Island",
                "Postcode": "10301",
                "Phone": "718-935-2402",
                "Districts Served": "31",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "718 Ocean Terrace",
                "Latitude": "40.608405",
                "Longitude": "-74.101919",
                "Community Board": "2",
                "Council District": "50",
                "Census Tract": "177",
                "BIN": "1015097",
                "BBL": "1008040001",
                "NTA": "Todt Hill-Emerson Hill-Heartland Village-Lighthouse Hill                   ",
                "Location 1": "(40.608405, -74.101919)",
            },
            {
                "\ufeffBorough": "Queens",
                "Postcode": "11354",
                "Phone": "718-935-2391",
                "Districts Served": "25, 26",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "30 48 Linden Place",
                "Latitude": "40.770185",
                "Longitude": "-73.832925",
                "Community Board": "7",
                "Council District": "20",
                "Census Tract": "869",
                "BIN": "4100749",
                "BBL": "4043700050",
                "NTA": "Flushing                                                                   ",
                "Location 1": "(40.770185, -73.832925)",
            },
            {
                "\ufeffBorough": "Queens",
                "Postcode": "11435",
                "Phone": "718-935-2393",
                "Districts Served": "27, 28, 29",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "90 27 Sutphin Boulevard",
                "Latitude": "40.70234",
                "Longitude": "-73.808148",
                "Community Board": "12",
                "Council District": "24",
                "Census Tract": "240",
                "BIN": "4206784",
                "BBL": "4096770007",
                "NTA": "Jamaica                                                                    ",
                "Location 1": "(40.70234, -73.808148)",
            },
            {
                "\ufeffBorough": "Queens",
                "Postcode": "11101",
                "Phone": "718-935-2386",
                "Districts Served": "24, 30",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "28 11 Queens Plaza",
                "Latitude": "40.75008",
                "Longitude": "-73.938208",
                "Community Board": "1",
                "Council District": "26",
                "Census Tract": "33",
                "BIN": "4005022",
                "BBL": "4004170002",
                "NTA": "Queensbridge-Ravenswood-Long Island City                                   ",
                "Location 1": "(40.75008, -73.938208)",
            },
            {
                "\ufeffBorough": "Manhattan",
                "Postcode": "10027",
                "Phone": "718-935-2385",
                "Districts Served": "3, 5, 6",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Address": "388 125th Street\n",
                "Latitude": "40.747629",
                "Longitude": "-73.99306",
                "Community Board": "5",
                "Council District": "3",
                "Census Tract": "95",
                "BIN": "",
                "BBL": "",
                "NTA": "",
                "Location 1": "(40.747629, -73.99306)",
            },
        ]
        self.assertEqual(actual, expected)

    def test_convert_xml_dict(self):
        resource = pyob.Resource(URL_XML, pyob.Connectivity.LOCAL)
        actual = pyob.convert(resource, [(pyob.InputType.XML, dict)])
        expected = {
            "response": {
                "row": {
                    "row": [
                        {
                            "@_id": "row-6i8g-hr3j-9zve",
                            "@_uuid": "00000000-0000-0000-CE12-EA21E43DEEB3",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-6i8g-hr3j-9zve",
                            "borough": "Bronx",
                            "zip_code": "10458",
                            "phone": "718-935-2178",
                            "districts_served": "7, 9, 10",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "1 Fordham Plaza",
                            "latitude": "40.860994",
                            "longitude": "-73.890073",
                            "community_board": "6",
                            "council_district": "15",
                            "census_tract": "387",
                            "nta": "Belmont",
                            "location_1": {"@latitude": "40.860994", "@longitude": "-73.890073"},
                        },
                        {
                            "@_id": "row-eeej.naj9-5pdg",
                            "@_uuid": "00000000-0000-0000-CCEA-3018E196BB8A",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-eeej.naj9-5pdg",
                            "borough": "Brooklyn",
                            "zip_code": "11230",
                            "phone": "718-935-2313",
                            "districts_served": "17, 18, 22",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "1780 Ocean Avenue",
                            "latitude": "40.618915",
                            "longitude": "-73.955115",
                            "community_board": "14",
                            "council_district": "48",
                            "census_tract": "538",
                            "bin": "3180747",
                            "bbl": "3067390077",
                            "nta": "Midwood",
                            "location_1": {"@latitude": "40.618915", "@longitude": "-73.955115"},
                        },
                        {
                            "@_id": "row-cdx4.9h2m~ypet",
                            "@_uuid": "00000000-0000-0000-7B54-22AE23D90E63",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-cdx4.9h2m~ypet",
                            "borough": "Brooklyn (Note: General Education Only)",
                            "zip_code": "11217",
                            "phone": "718-935-2371",
                            "districts_served": "13, 14, 15, 16",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "29 Fort Greene Place\n(Note: General Education Only)",
                            "latitude": "40.688834",
                            "longitude": "-73.976905",
                            "community_board": "2",
                            "council_district": "35",
                            "census_tract": "33",
                            "bin": "3058752",
                            "bbl": "3020980013",
                            "nta": "Fort Greene",
                            "location_1": {"@latitude": "40.688834", "@longitude": "-73.976905"},
                        },
                        {
                            "@_id": "row-5bhh_guh2_qmbh",
                            "@_uuid": "00000000-0000-0000-1DB1-07B23244B75C",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-5bhh_guh2_qmbh",
                            "borough": "Brooklyn (Note: Special Education Only)",
                            "zip_code": "11201",
                            "phone": "718-935-4908",
                            "districts_served": "13, 14, 15, 16",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "131 Livingston Street\n(Note: Special Education Only)",
                            "latitude": "40.690743",
                            "longitude": "-73.988605",
                            "community_board": "2",
                            "council_district": "33",
                            "census_tract": "37",
                            "bin": "3000420",
                            "bbl": "3001540001",
                            "nta": "DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum Hill",
                            "location_1": {"@latitude": "40.690743", "@longitude": "-73.988605"},
                        },
                        {
                            "@_id": "row-grua.rcwh.w5mi",
                            "@_uuid": "00000000-0000-0000-0E02-3253DD395F4D",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-grua.rcwh.w5mi",
                            "borough": "Brooklyn",
                            "zip_code": "11209",
                            "phone": "718-935-2331",
                            "districts_served": "20, 21",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "415 89th Street",
                            "latitude": "40.619931",
                            "longitude": "-74.028086",
                            "community_board": "10",
                            "council_district": "43",
                            "census_tract": "160",
                            "bin": "3154215",
                            "bbl": "3060650043",
                            "nta": "Bay Ridge",
                            "location_1": {"@latitude": "40.619931", "@longitude": "-74.028086"},
                        },
                        {
                            "@_id": "row-eyc7~sa8d-i2ye",
                            "@_uuid": "00000000-0000-0000-5FB7-20EA903A05BA",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-eyc7~sa8d-i2ye",
                            "borough": "Brooklyn",
                            "zip_code": "11233",
                            "phone": "718-935-2340",
                            "districts_served": "19, 23, 32",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "1665 St Mark's Avenue",
                            "latitude": "40.673138",
                            "longitude": "-73.912024",
                            "community_board": "16",
                            "council_district": "41",
                            "census_tract": "36501",
                            "bin": "3039123",
                            "bbl": "3014540054",
                            "nta": "Ocean Hill",
                            "location_1": {"@latitude": "40.673138", "@longitude": "-73.912024"},
                        },
                        {
                            "@_id": "row-ksm7~bhh7.eqes",
                            "@_uuid": "00000000-0000-0000-78C6-9B93B2323305",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-ksm7~bhh7.eqes",
                            "borough": "Bronx",
                            "zip_code": "10462",
                            "phone": "718-935-2278",
                            "districts_served": "8, 11, 12",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "1230 Zerega Avenue",
                            "latitude": "40.833586",
                            "longitude": "-73.845099",
                            "community_board": "9",
                            "council_district": "13",
                            "census_tract": "96",
                            "bin": "2027195",
                            "bbl": "2038420002",
                            "nta": "Westchester-Unionport",
                            "location_1": {"@latitude": "40.833586", "@longitude": "-73.845099"},
                        },
                        {
                            "@_id": "row-v7pq_vrkp.6aqq",
                            "@_uuid": "00000000-0000-0000-98CB-48941877F408",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-v7pq_vrkp.6aqq",
                            "borough": "Manhattan",
                            "zip_code": "10001",
                            "phone": "718-935-2383",
                            "districts_served": "1, 2, 4",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "333 Seventh Avenue",
                            "latitude": "40.747629",
                            "longitude": "-73.99306",
                            "community_board": "5",
                            "council_district": "3",
                            "census_tract": "95",
                            "bin": "1015097",
                            "bbl": "1008040001",
                            "nta": "Midtown-Midtown South",
                            "location_1": {"@latitude": "40.747629", "@longitude": "-73.99306"},
                        },
                        {
                            "@_id": "row-rhvp-hxsg_mgpf",
                            "@_uuid": "00000000-0000-0000-2654-0E8E5DE5516A",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-rhvp-hxsg_mgpf",
                            "borough": "Staten Island",
                            "zip_code": "10301",
                            "phone": "718-935-2402",
                            "districts_served": "31",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "718 Ocean Terrace",
                            "latitude": "40.608405",
                            "longitude": "-74.101919",
                            "community_board": "2",
                            "council_district": "50",
                            "census_tract": "177",
                            "bin": "1015097",
                            "bbl": "1008040001",
                            "nta": "Todt Hill-Emerson Hill-Heartland Village-Lighthouse Hill",
                            "location_1": {"@latitude": "40.608405", "@longitude": "-74.101919"},
                        },
                        {
                            "@_id": "row-h5zk-e2bj.wzf9",
                            "@_uuid": "00000000-0000-0000-C5D4-D9C1D0D70C4C",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-h5zk-e2bj.wzf9",
                            "borough": "Queens",
                            "zip_code": "11354",
                            "phone": "718-935-2391",
                            "districts_served": "25, 26",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "30 48 Linden Place",
                            "latitude": "40.770185",
                            "longitude": "-73.832925",
                            "community_board": "7",
                            "council_district": "20",
                            "census_tract": "869",
                            "bin": "4100749",
                            "bbl": "4043700050",
                            "nta": "Flushing",
                            "location_1": {"@latitude": "40.770185", "@longitude": "-73.832925"},
                        },
                        {
                            "@_id": "row-a47k-cngf~ym45",
                            "@_uuid": "00000000-0000-0000-5C94-E84AD56B56AC",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-a47k-cngf~ym45",
                            "borough": "Queens",
                            "zip_code": "11435",
                            "phone": "718-935-2393",
                            "districts_served": "27, 28, 29",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "90 27 Sutphin Boulevard",
                            "latitude": "40.70234",
                            "longitude": "-73.808148",
                            "community_board": "12",
                            "council_district": "24",
                            "census_tract": "240",
                            "bin": "4206784",
                            "bbl": "4096770007",
                            "nta": "Jamaica",
                            "location_1": {"@latitude": "40.70234", "@longitude": "-73.808148"},
                        },
                        {
                            "@_id": "row-vq7r-m4yb_vwn2",
                            "@_uuid": "00000000-0000-0000-BA4B-C2FB27F1C66C",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-vq7r-m4yb_vwn2",
                            "borough": "Queens",
                            "zip_code": "11101",
                            "phone": "718-935-2386",
                            "districts_served": "24, 30",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "28 11 Queens Plaza",
                            "latitude": "40.75008",
                            "longitude": "-73.938208",
                            "community_board": "1",
                            "council_district": "26",
                            "census_tract": "33",
                            "bin": "4005022",
                            "bbl": "4004170002",
                            "nta": "Queensbridge-Ravenswood-Long Island City",
                            "location_1": {"@latitude": "40.75008", "@longitude": "-73.938208"},
                        },
                        {
                            "@_id": "row-vs8h.2k5f-hk5v",
                            "@_uuid": "00000000-0000-0000-F2E5-6BFF1595FF1E",
                            "@_position": "0",
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-vs8h.2k5f-hk5v",
                            "borough": "Manhattan",
                            "zip_code": "10027",
                            "phone": "718-935-2385",
                            "districts_served": "3, 5, 6",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "address": "388 125th Street",
                            "latitude": "40.747629",
                            "longitude": "-73.99306",
                            "community_board": "5",
                            "council_district": "3",
                            "census_tract": "95",
                            "location_1": {"@latitude": "40.747629", "@longitude": "-73.99306"},
                        },
                    ]
                }
            }
        }
        self.assertEqual(actual, expected)

    def test_convert_xlsx_dict(self):
        resource = pyob.Resource(URL_XLSX, pyob.Connectivity.LOCAL)
        actual = pyob.convert(resource, [(pyob.InputType.XLSX, dict)])
        expected = {
            "Sheet1": {
                "Abbreviation": {0: "MN", 1: "BK", 2: "QN", 3: "BX", 4: "SI"},
                "Borough": {0: "Manhattan", 1: "Brooklyn", 2: "Queens", 3: "The Bronx", 4: "Staten Island"},
                "Index": {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
            },
            "Sheet2": {
                "Abbreviation": {0: "XM", 1: "XB", 2: "XQ", 3: "XX", 4: "XS"},
                "Borough": {
                    0: "Not Manhattan",
                    1: "Not Brooklyn",
                    2: "Not Queens",
                    3: "Not The Bronx",
                    4: "Not Staten Island",
                },
                "Index": {0: 6, 1: 7, 2: 8, 3: 9, 4: 10},
            },
        }
        self.assertEqual(actual, expected)

    def test_convert_error(self):
        resource = pyob.Resource(URL_JSON, pyob.Connectivity.LOCAL)
        with self.assertRaises(TypeError):
            pyob.convert(resource, [(pyob.InputType.JSON, OUTPUT_TYPE_UNSUPPORTED)])

    def test_from_url(self):
        actual = pyob.from_url(URL_JSON)
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

    def test_from_url_error(self):
        with self.assertRaises(TypeError):
            pyob.from_url(URL_JSON, OUTPUT_TYPE_UNSUPPORTED)


if __name__ == "__main__":
    unittest.main()
