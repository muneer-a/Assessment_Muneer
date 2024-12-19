import json
import pandas as pd
from jsonschema import validate

filename='dataset'

my_json = json.load(open(filename))
validate(instance=my_json, schema=schema)
print(my_json)

filtered = list[filter(lambda x : x['column_position']>0,my_json)]

def validate(filename):
    with open(filename) as file:
        try:
            data = json.load(file)
            print("Valid JSON")   
            return data
        except json.decoder.JSONDecodeError:
            print("Invalid JSON")