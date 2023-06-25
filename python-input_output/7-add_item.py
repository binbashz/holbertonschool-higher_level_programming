#!/usr/bin/python3

""" 7. Load, add, save
Add all arguments to a Python list, and then save them to a file
"""

import sys
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
data = {}

if Path(filename).is_file():
    data = load_from_json_file(filename)

my_list = data.get('my_list', [])
my_list.extend(sys.argv[1:])

data['my_list'] = my_list
save_to_json_file(data, filename)
