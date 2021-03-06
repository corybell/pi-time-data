from json import load, dump
from sys import stdout

def collection_to_dict(data):
  new_dict = {}
  for item in data:
    value = item.get('value')
    label = item.get('label')
    new_dict[value] = label
  return new_dict

def debug_log(msg: str):
  print(msg, file=stdout)

def get_str(payload: dict, key: str):
  val = payload.get(key)
  if val is not None and isinstance(val, str):
    return val.strip()
  return None

def read_file(file: str):
  with open(file) as data_file:
    return load(data_file)

def write_file(file: str, data: dict):
  with open(file, 'w') as outfile:  
      dump(data, outfile, indent=2)

