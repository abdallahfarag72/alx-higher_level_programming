#!/usr/bin/python3

"""
Script that adds all arguments to a Python list and saves them to a file
"""


import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

filename = "add_item.json"
items = []

if path.exists(filename):
    items = load_from_json_file(filename)

items.extend(args)
save_to_json_file(items, filename)
