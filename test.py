from pprint import pprint

import pyobjectify

#========== JSON FILE ==========

json_file = open("./test/example.json", 'r')
json_dict = pyobjectify.json_file_to_dict(json_file)

pprint(json_dict['quiz'])

#========== JSON API ==========

json_dict = pyobjectify.json_api_to_dict("https://jsonplaceholder.typicode.com/users")

pprint(json_dict[:3])         #only see first 3 objects
pprint(json_dict[0]["name"])  #query an object

#========== CSV FILE ==========

csv_file = open("./test/example.csv", 'r')
csv_list = pyobjectify.csv_file_to_list(csv_file)

pprint(csv_list[:3])            # only see first 3 rows
pprint(csv_list[0]["Address"])  # query a row

#========== TSV FILE ==========

tsv_file = open("./test/example.tsv", 'r')
tsv_list = pyobjectify.tsv_file_to_list(tsv_file)

pprint(tsv_list[:3])            # only see first 3 rows
pprint(tsv_list[0]["Address"])  # query a row

#========== XML FILE ==========

xml_file = open("./test/example.xml", 'r')
xml_dict = pyobjectify.xml_file_to_dict(xml_file)

pprint(xml_dict['response']['row']['row'][0])  # query one row