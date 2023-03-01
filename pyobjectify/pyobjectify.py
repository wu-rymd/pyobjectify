import requests
import json
import csv
import xmltodict


def json_file_to_dict(file_obj):
    json_obj = json.load(file_obj)
    return json_obj


def json_api_to_dict(url):
    response = requests.get(url)
    json_obj = response.json()
    return json_obj


def csv_file_to_list(file_obj):
    row_dict = csv.DictReader(file_obj)
    return list(row_dict)


def tsv_file_to_list(file_obj):
    row_dict = csv.DictReader(file_obj, delimiter="\t")
    return list(row_dict)


def xml_file_to_dict(file_obj):
    xml_dict = xmltodict.parse(file_obj.read())
    return xml_dict
