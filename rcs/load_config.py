import json

def load_config():
  configs = {}
  with open('config.json') as json_file:
    configs = json.load(json_file)
  return configs
