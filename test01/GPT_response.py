import json
import pprint
from pprint import pprint

with open('response.json', 'r') as f:
    response = json.load(f)


pprint(response)