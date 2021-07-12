from json import load, dump
from uuid import uuid4

def get_str(payload, key):
  val = payload.get(key)
  if val is not None and isinstance(val, str):
    return val.strip()
  return None

def read_file(file):
  with open(file) as data_file:
    return load(data_file)

def write_file(file, data):
  with open(file, 'w') as outfile:  
      dump(data, outfile, indent=2)

