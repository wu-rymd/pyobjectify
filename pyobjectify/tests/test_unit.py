import pyobjectify

import os
import unittest

DIR = os.path.dirname(__file__) or "."


class TestPyobjectify(unittest.TestCase):
    def test_json_file_to_dict(self):
        json_file = open(f"{DIR}/data/example.json", "r")
        actual = pyobjectify.json_file_to_dict(json_file)
        expected = {
            "quiz": {
                "maths": {
                    "q1": {"answer": "12", "options": ["10", "11", "12", "13"], "question": "5 + 7 = ?"},
                    "q2": {"answer": "4", "options": ["1", "2", "3", "4"], "question": "12 - 8 = ?"},
                },
                "sport": {
                    "q1": {
                        "answer": "Huston Rocket",
                        "options": ["New York Bulls", "Los Angeles Kings", "Golden State Warriros", "Huston Rocket"],
                        "question": "Which one is correct team name in NBA?",
                    }
                },
            }
        }
        json_file.close()
        self.assertEqual(actual, expected)

    def test_json_api_to_dict(self):
        actual = pyobjectify.json_api_to_dict("https://api.rymd.app/data")
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

    def test_csv_file_to_list(self):
        csv_file = open(f"{DIR}/data/example.csv", "r")
        expected = pyobjectify.csv_file_to_list(csv_file)
        actual = [
            {
                "Address": "1 Fordham Plaza",
                "BBL": "",
                "BIN": "",
                "Borough": "Bronx",
                "Census Tract": "387",
                "Community Board": "6",
                "Council District": "15",
                "Districts Served": "7, 9, 10",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.860994",
                "Location 1": "(40.860994, -73.890073)",
                "Longitude": "-73.890073",
                "NTA": "Belmont                                                                    ",
                "Phone": "718-935-2178",
                "Postcode": "10458",
            },
            {
                "Address": "1780 Ocean Avenue\n",
                "BBL": "3067390077",
                "BIN": "3180747",
                "Borough": "Brooklyn",
                "Census Tract": "538",
                "Community Board": "14",
                "Council District": "48",
                "Districts Served": "17, 18, 22",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.618915",
                "Location 1": "(40.618915, -73.955115)",
                "Longitude": "-73.955115",
                "NTA": "Midwood                                                                    ",
                "Phone": "718-935-2313",
                "Postcode": "11230",
            },
            {
                "Address": "29 Fort Greene Place\n(Note: General Education Only)",
                "BBL": "3020980013",
                "BIN": "3058752",
                "Borough": "Brooklyn (Note: General Education Only)",
                "Census Tract": "33",
                "Community Board": "2",
                "Council District": "35",
                "Districts Served": "13, 14, 15, 16",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.688834",
                "Location 1": "(40.688834, -73.976905)",
                "Longitude": "-73.976905",
                "NTA": "Fort " "Greene                                                                ",
                "Phone": "718-935-2371",
                "Postcode": "11217",
            },
            {
                "Address": "131 Livingston Street\n(Note: Special Education Only)",
                "BBL": "3001540001",
                "BIN": "3000420",
                "Borough": "Brooklyn (Note: Special Education Only)",
                "Census Tract": "37",
                "Community Board": "2",
                "Council District": "33",
                "Districts Served": "13, 14, 15, 16",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.690743",
                "Location 1": "(40.690743, -73.988605)",
                "Longitude": "-73.988605",
                "NTA": "DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum " "Hill                           ",
                "Phone": "718-935-4908",
                "Postcode": "11201",
            },
            {
                "Address": "415 89th Street\n",
                "BBL": "3060650043",
                "BIN": "3154215",
                "Borough": "Brooklyn",
                "Census Tract": "160",
                "Community Board": "10",
                "Council District": "43",
                "Districts Served": "20, 21",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.619931",
                "Location 1": "(40.619931, -74.028086)",
                "Longitude": "-74.028086",
                "NTA": "Bay " "Ridge                                                                  ",
                "Phone": "718-935-2331",
                "Postcode": "11209",
            },
            {
                "Address": "1665 St Mark's Avenue\n",
                "BBL": "3014540054",
                "BIN": "3039123",
                "Borough": "Brooklyn",
                "Census Tract": "36501",
                "Community Board": "16",
                "Council District": "41",
                "Districts Served": "19, 23, 32",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.673138",
                "Location 1": "(40.673138, -73.912024)",
                "Longitude": "-73.912024",
                "NTA": "Ocean " "Hill                                                                 ",
                "Phone": "718-935-2340",
                "Postcode": "11233",
            },
            {
                "Address": "1230 Zerega Avenue\n ",
                "BBL": "2038420002",
                "BIN": "2027195",
                "Borough": "Bronx",
                "Census Tract": "96",
                "Community Board": "9",
                "Council District": "13",
                "Districts Served": "8, 11, 12",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.833586",
                "Location 1": "(40.833586, -73.845099)",
                "Longitude": "-73.845099",
                "NTA": "Westchester-Unionport                                                      ",
                "Phone": "718-935-2278",
                "Postcode": "10462",
            },
            {
                "Address": "333 Seventh Avenue\n",
                "BBL": "1008040001",
                "BIN": "1015097",
                "Borough": "Manhattan",
                "Census Tract": "95",
                "Community Board": "5",
                "Council District": "3",
                "Districts Served": "1, 2, 4",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.747629",
                "Location 1": "(40.747629, -73.99306)",
                "Longitude": "-73.99306",
                "NTA": "Midtown-Midtown " "South                                                      ",
                "Phone": "718-935-2383",
                "Postcode": "10001",
            },
            {
                "Address": "718 Ocean Terrace",
                "BBL": "1008040001",
                "BIN": "1015097",
                "Borough": "Staten Island",
                "Census Tract": "177",
                "Community Board": "2",
                "Council District": "50",
                "Districts Served": "31",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.608405",
                "Location 1": "(40.608405, -74.101919)",
                "Longitude": "-74.101919",
                "NTA": "Todt Hill-Emerson Hill-Heartland Village-Lighthouse " "Hill                   ",
                "Phone": "718-935-2402",
                "Postcode": "10301",
            },
            {
                "Address": "30 48 Linden Place",
                "BBL": "4043700050",
                "BIN": "4100749",
                "Borough": "Queens",
                "Census Tract": "869",
                "Community Board": "7",
                "Council District": "20",
                "Districts Served": "25, 26",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.770185",
                "Location 1": "(40.770185, -73.832925)",
                "Longitude": "-73.832925",
                "NTA": "Flushing                                                                   ",
                "Phone": "718-935-2391",
                "Postcode": "11354",
            },
            {
                "Address": "90 27 Sutphin Boulevard",
                "BBL": "4096770007",
                "BIN": "4206784",
                "Borough": "Queens",
                "Census Tract": "240",
                "Community Board": "12",
                "Council District": "24",
                "Districts Served": "27, 28, 29",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.70234",
                "Location 1": "(40.70234, -73.808148)",
                "Longitude": "-73.808148",
                "NTA": "Jamaica                                                                    ",
                "Phone": "718-935-2393",
                "Postcode": "11435",
            },
            {
                "Address": "28 11 Queens Plaza",
                "BBL": "4004170002",
                "BIN": "4005022",
                "Borough": "Queens",
                "Census Tract": "33",
                "Community Board": "1",
                "Council District": "26",
                "Districts Served": "24, 30",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.75008",
                "Location 1": "(40.75008, -73.938208)",
                "Longitude": "-73.938208",
                "NTA": "Queensbridge-Ravenswood-Long Island " "City                                   ",
                "Phone": "718-935-2386",
                "Postcode": "11101",
            },
            {
                "Address": "388 125th Street\n",
                "BBL": "",
                "BIN": "",
                "Borough": "Manhattan",
                "Census Tract": "95",
                "Community Board": "5",
                "Council District": "3",
                "Districts Served": "3, 5, 6",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.747629",
                "Location 1": "(40.747629, -73.99306)",
                "Longitude": "-73.99306",
                "NTA": "",
                "Phone": "718-935-2385",
                "Postcode": "10027",
            },
        ]
        csv_file.close()
        self.assertEqual(actual, expected)

    def test_tsv_file_to_list(self):
        tsv_file = open(f"{DIR}/data/example.tsv", "r")
        expected = pyobjectify.tsv_file_to_list(tsv_file)
        actual = [
            {
                "Address": "1 Fordham Plaza",
                "BBL": "",
                "BIN": "",
                "Census Tract": "387",
                "Community Board": "6",
                "Council District": "15",
                "Districts Served": "7, 9, 10",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.860994",
                "Location 1": "(40.860994, -73.890073)",
                "Longitude": "-73.890073",
                "NTA": "Belmont                                                                    ",
                "Phone": "718-935-2178",
                "Postcode": "10458",
                "\ufeffBorough": "Bronx",
            },
            {
                "Address": "1780 Ocean Avenue\n",
                "BBL": "3067390077",
                "BIN": "3180747",
                "Census Tract": "538",
                "Community Board": "14",
                "Council District": "48",
                "Districts Served": "17, 18, 22",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.618915",
                "Location 1": "(40.618915, -73.955115)",
                "Longitude": "-73.955115",
                "NTA": "Midwood                                                                    ",
                "Phone": "718-935-2313",
                "Postcode": "11230",
                "\ufeffBorough": "Brooklyn",
            },
            {
                "Address": "29 Fort Greene Place\n(Note: General Education Only)",
                "BBL": "3020980013",
                "BIN": "3058752",
                "Census Tract": "33",
                "Community Board": "2",
                "Council District": "35",
                "Districts Served": "13, 14, 15, 16",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.688834",
                "Location 1": "(40.688834, -73.976905)",
                "Longitude": "-73.976905",
                "NTA": "Fort " "Greene                                                                ",
                "Phone": "718-935-2371",
                "Postcode": "11217",
                "\ufeffBorough": "Brooklyn (Note: General Education Only)",
            },
            {
                "Address": "131 Livingston Street\n(Note: Special Education Only)",
                "BBL": "3001540001",
                "BIN": "3000420",
                "Census Tract": "37",
                "Community Board": "2",
                "Council District": "33",
                "Districts Served": "13, 14, 15, 16",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.690743",
                "Location 1": "(40.690743, -73.988605)",
                "Longitude": "-73.988605",
                "NTA": "DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum " "Hill                           ",
                "Phone": "718-935-4908",
                "Postcode": "11201",
                "\ufeffBorough": "Brooklyn (Note: Special Education Only)",
            },
            {
                "Address": "415 89th Street\n",
                "BBL": "3060650043",
                "BIN": "3154215",
                "Census Tract": "160",
                "Community Board": "10",
                "Council District": "43",
                "Districts Served": "20, 21",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.619931",
                "Location 1": "(40.619931, -74.028086)",
                "Longitude": "-74.028086",
                "NTA": "Bay " "Ridge                                                                  ",
                "Phone": "718-935-2331",
                "Postcode": "11209",
                "\ufeffBorough": "Brooklyn",
            },
            {
                "Address": "1665 St Mark's Avenue\n",
                "BBL": "3014540054",
                "BIN": "3039123",
                "Census Tract": "36501",
                "Community Board": "16",
                "Council District": "41",
                "Districts Served": "19, 23, 32",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.673138",
                "Location 1": "(40.673138, -73.912024)",
                "Longitude": "-73.912024",
                "NTA": "Ocean " "Hill                                                                 ",
                "Phone": "718-935-2340",
                "Postcode": "11233",
                "\ufeffBorough": "Brooklyn",
            },
            {
                "Address": "1230 Zerega Avenue\n ",
                "BBL": "2038420002",
                "BIN": "2027195",
                "Census Tract": "96",
                "Community Board": "9",
                "Council District": "13",
                "Districts Served": "8, 11, 12",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.833586",
                "Location 1": "(40.833586, -73.845099)",
                "Longitude": "-73.845099",
                "NTA": "Westchester-Unionport                                                      ",
                "Phone": "718-935-2278",
                "Postcode": "10462",
                "\ufeffBorough": "Bronx",
            },
            {
                "Address": "333 Seventh Avenue\n",
                "BBL": "1008040001",
                "BIN": "1015097",
                "Census Tract": "95",
                "Community Board": "5",
                "Council District": "3",
                "Districts Served": "1, 2, 4",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.747629",
                "Location 1": "(40.747629, -73.99306)",
                "Longitude": "-73.99306",
                "NTA": "Midtown-Midtown " "South                                                      ",
                "Phone": "718-935-2383",
                "Postcode": "10001",
                "\ufeffBorough": "Manhattan",
            },
            {
                "Address": "718 Ocean Terrace",
                "BBL": "1008040001",
                "BIN": "1015097",
                "Census Tract": "177",
                "Community Board": "2",
                "Council District": "50",
                "Districts Served": "31",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.608405",
                "Location 1": "(40.608405, -74.101919)",
                "Longitude": "-74.101919",
                "NTA": "Todt Hill-Emerson Hill-Heartland Village-Lighthouse " "Hill                   ",
                "Phone": "718-935-2402",
                "Postcode": "10301",
                "\ufeffBorough": "Staten Island",
            },
            {
                "Address": "30 48 Linden Place",
                "BBL": "4043700050",
                "BIN": "4100749",
                "Census Tract": "869",
                "Community Board": "7",
                "Council District": "20",
                "Districts Served": "25, 26",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.770185",
                "Location 1": "(40.770185, -73.832925)",
                "Longitude": "-73.832925",
                "NTA": "Flushing                                                                   ",
                "Phone": "718-935-2391",
                "Postcode": "11354",
                "\ufeffBorough": "Queens",
            },
            {
                "Address": "90 27 Sutphin Boulevard",
                "BBL": "4096770007",
                "BIN": "4206784",
                "Census Tract": "240",
                "Community Board": "12",
                "Council District": "24",
                "Districts Served": "27, 28, 29",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.70234",
                "Location 1": "(40.70234, -73.808148)",
                "Longitude": "-73.808148",
                "NTA": "Jamaica                                                                    ",
                "Phone": "718-935-2393",
                "Postcode": "11435",
                "\ufeffBorough": "Queens",
            },
            {
                "Address": "28 11 Queens Plaza",
                "BBL": "4004170002",
                "BIN": "4005022",
                "Census Tract": "33",
                "Community Board": "1",
                "Council District": "26",
                "Districts Served": "24, 30",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.75008",
                "Location 1": "(40.75008, -73.938208)",
                "Longitude": "-73.938208",
                "NTA": "Queensbridge-Ravenswood-Long Island " "City                                   ",
                "Phone": "718-935-2386",
                "Postcode": "11101",
                "\ufeffBorough": "Queens",
            },
            {
                "Address": "388 125th Street\n",
                "BBL": "",
                "BIN": "",
                "Census Tract": "95",
                "Community Board": "5",
                "Council District": "3",
                "Districts Served": "3, 5, 6",
                "Hours": "Monday-Friday, 8:00am-3:00pm",
                "Latitude": "40.747629",
                "Location 1": "(40.747629, -73.99306)",
                "Longitude": "-73.99306",
                "NTA": "",
                "Phone": "718-935-2385",
                "Postcode": "10027",
                "\ufeffBorough": "Manhattan",
            },
        ]
        tsv_file.close()
        self.assertEqual(actual, expected)

    def test_xml_file_to_dict(self):
        xml_file = open(f"{DIR}/data/example.xml", "r")
        expected = pyobjectify.xml_file_to_dict(xml_file)
        actual = {
            "response": {
                "row": {
                    "row": [
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-6i8g-hr3j-9zve",
                            "@_id": "row-6i8g-hr3j-9zve",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-CE12-EA21E43DEEB3",
                            "address": "1 Fordham Plaza",
                            "borough": "Bronx",
                            "census_tract": "387",
                            "community_board": "6",
                            "council_district": "15",
                            "districts_served": "7, 9, 10",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.860994",
                            "location_1": {
                                "@latitude": "40.860994",
                                "@longitude": "-73.890073",
                            },
                            "longitude": "-73.890073",
                            "nta": "Belmont",
                            "phone": "718-935-2178",
                            "zip_code": "10458",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-eeej.naj9-5pdg",
                            "@_id": "row-eeej.naj9-5pdg",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-CCEA-3018E196BB8A",
                            "address": "1780 Ocean Avenue",
                            "bbl": "3067390077",
                            "bin": "3180747",
                            "borough": "Brooklyn",
                            "census_tract": "538",
                            "community_board": "14",
                            "council_district": "48",
                            "districts_served": "17, 18, 22",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.618915",
                            "location_1": {
                                "@latitude": "40.618915",
                                "@longitude": "-73.955115",
                            },
                            "longitude": "-73.955115",
                            "nta": "Midwood",
                            "phone": "718-935-2313",
                            "zip_code": "11230",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-cdx4.9h2m~ypet",
                            "@_id": "row-cdx4.9h2m~ypet",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-7B54-22AE23D90E63",
                            "address": "29 Fort Greene Place\n" "(Note: General Education Only)",
                            "bbl": "3020980013",
                            "bin": "3058752",
                            "borough": "Brooklyn (Note: General Education " "Only)",
                            "census_tract": "33",
                            "community_board": "2",
                            "council_district": "35",
                            "districts_served": "13, 14, 15, 16",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.688834",
                            "location_1": {
                                "@latitude": "40.688834",
                                "@longitude": "-73.976905",
                            },
                            "longitude": "-73.976905",
                            "nta": "Fort Greene",
                            "phone": "718-935-2371",
                            "zip_code": "11217",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-5bhh_guh2_qmbh",
                            "@_id": "row-5bhh_guh2_qmbh",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-1DB1-07B23244B75C",
                            "address": "131 Livingston Street\n" "(Note: Special Education Only)",
                            "bbl": "3001540001",
                            "bin": "3000420",
                            "borough": "Brooklyn (Note: Special Education " "Only)",
                            "census_tract": "37",
                            "community_board": "2",
                            "council_district": "33",
                            "districts_served": "13, 14, 15, 16",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.690743",
                            "location_1": {
                                "@latitude": "40.690743",
                                "@longitude": "-73.988605",
                            },
                            "longitude": "-73.988605",
                            "nta": "DUMBO-Vinegar Hill-Downtown " "Brooklyn-Boerum Hill",
                            "phone": "718-935-4908",
                            "zip_code": "11201",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-grua.rcwh.w5mi",
                            "@_id": "row-grua.rcwh.w5mi",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-0E02-3253DD395F4D",
                            "address": "415 89th Street",
                            "bbl": "3060650043",
                            "bin": "3154215",
                            "borough": "Brooklyn",
                            "census_tract": "160",
                            "community_board": "10",
                            "council_district": "43",
                            "districts_served": "20, 21",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.619931",
                            "location_1": {
                                "@latitude": "40.619931",
                                "@longitude": "-74.028086",
                            },
                            "longitude": "-74.028086",
                            "nta": "Bay Ridge",
                            "phone": "718-935-2331",
                            "zip_code": "11209",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-eyc7~sa8d-i2ye",
                            "@_id": "row-eyc7~sa8d-i2ye",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-5FB7-20EA903A05BA",
                            "address": "1665 St Mark's Avenue",
                            "bbl": "3014540054",
                            "bin": "3039123",
                            "borough": "Brooklyn",
                            "census_tract": "36501",
                            "community_board": "16",
                            "council_district": "41",
                            "districts_served": "19, 23, 32",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.673138",
                            "location_1": {
                                "@latitude": "40.673138",
                                "@longitude": "-73.912024",
                            },
                            "longitude": "-73.912024",
                            "nta": "Ocean Hill",
                            "phone": "718-935-2340",
                            "zip_code": "11233",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-ksm7~bhh7.eqes",
                            "@_id": "row-ksm7~bhh7.eqes",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-78C6-9B93B2323305",
                            "address": "1230 Zerega Avenue",
                            "bbl": "2038420002",
                            "bin": "2027195",
                            "borough": "Bronx",
                            "census_tract": "96",
                            "community_board": "9",
                            "council_district": "13",
                            "districts_served": "8, 11, 12",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.833586",
                            "location_1": {
                                "@latitude": "40.833586",
                                "@longitude": "-73.845099",
                            },
                            "longitude": "-73.845099",
                            "nta": "Westchester-Unionport",
                            "phone": "718-935-2278",
                            "zip_code": "10462",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-v7pq_vrkp.6aqq",
                            "@_id": "row-v7pq_vrkp.6aqq",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-98CB-48941877F408",
                            "address": "333 Seventh Avenue",
                            "bbl": "1008040001",
                            "bin": "1015097",
                            "borough": "Manhattan",
                            "census_tract": "95",
                            "community_board": "5",
                            "council_district": "3",
                            "districts_served": "1, 2, 4",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.747629",
                            "location_1": {"@latitude": "40.747629", "@longitude": "-73.99306"},
                            "longitude": "-73.99306",
                            "nta": "Midtown-Midtown South",
                            "phone": "718-935-2383",
                            "zip_code": "10001",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-rhvp-hxsg_mgpf",
                            "@_id": "row-rhvp-hxsg_mgpf",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-2654-0E8E5DE5516A",
                            "address": "718 Ocean Terrace",
                            "bbl": "1008040001",
                            "bin": "1015097",
                            "borough": "Staten Island",
                            "census_tract": "177",
                            "community_board": "2",
                            "council_district": "50",
                            "districts_served": "31",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.608405",
                            "location_1": {
                                "@latitude": "40.608405",
                                "@longitude": "-74.101919",
                            },
                            "longitude": "-74.101919",
                            "nta": "Todt Hill-Emerson Hill-Heartland " "Village-Lighthouse Hill",
                            "phone": "718-935-2402",
                            "zip_code": "10301",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-h5zk-e2bj.wzf9",
                            "@_id": "row-h5zk-e2bj.wzf9",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-C5D4-D9C1D0D70C4C",
                            "address": "30 48 Linden Place",
                            "bbl": "4043700050",
                            "bin": "4100749",
                            "borough": "Queens",
                            "census_tract": "869",
                            "community_board": "7",
                            "council_district": "20",
                            "districts_served": "25, 26",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.770185",
                            "location_1": {
                                "@latitude": "40.770185",
                                "@longitude": "-73.832925",
                            },
                            "longitude": "-73.832925",
                            "nta": "Flushing",
                            "phone": "718-935-2391",
                            "zip_code": "11354",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-a47k-cngf~ym45",
                            "@_id": "row-a47k-cngf~ym45",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-5C94-E84AD56B56AC",
                            "address": "90 27 Sutphin Boulevard",
                            "bbl": "4096770007",
                            "bin": "4206784",
                            "borough": "Queens",
                            "census_tract": "240",
                            "community_board": "12",
                            "council_district": "24",
                            "districts_served": "27, 28, 29",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.70234",
                            "location_1": {"@latitude": "40.70234", "@longitude": "-73.808148"},
                            "longitude": "-73.808148",
                            "nta": "Jamaica",
                            "phone": "718-935-2393",
                            "zip_code": "11435",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-vq7r-m4yb_vwn2",
                            "@_id": "row-vq7r-m4yb_vwn2",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-BA4B-C2FB27F1C66C",
                            "address": "28 11 Queens Plaza",
                            "bbl": "4004170002",
                            "bin": "4005022",
                            "borough": "Queens",
                            "census_tract": "33",
                            "community_board": "1",
                            "council_district": "26",
                            "districts_served": "24, 30",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.75008",
                            "location_1": {"@latitude": "40.75008", "@longitude": "-73.938208"},
                            "longitude": "-73.938208",
                            "nta": "Queensbridge-Ravenswood-Long Island " "City",
                            "phone": "718-935-2386",
                            "zip_code": "11101",
                        },
                        {
                            "@_address": "https://data.cityofnewyork.us/resource/vz8c-29aj/row-vs8h.2k5f-hk5v",
                            "@_id": "row-vs8h.2k5f-hk5v",
                            "@_position": "0",
                            "@_uuid": "00000000-0000-0000-F2E5-6BFF1595FF1E",
                            "address": "388 125th Street",
                            "borough": "Manhattan",
                            "census_tract": "95",
                            "community_board": "5",
                            "council_district": "3",
                            "districts_served": "3, 5, 6",
                            "hours": "Monday-Friday, 8:00am-3:00pm",
                            "latitude": "40.747629",
                            "location_1": {"@latitude": "40.747629", "@longitude": "-73.99306"},
                            "longitude": "-73.99306",
                            "phone": "718-935-2385",
                            "zip_code": "10027",
                        },
                    ]
                }
            }
        }
        xml_file.close()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()