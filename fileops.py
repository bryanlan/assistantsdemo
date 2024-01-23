import json

import os
import re

def read_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {filepath}")
        return None

def write_json_file(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def read_text_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def write_text_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as file:
        for item in content:
            file.write(str(item) + '\n')  # Write each item on a new line

