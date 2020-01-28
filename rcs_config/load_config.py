from json import load, dump

def load_config():
  configs = {}
  with open('rcs.conf.json') as json_file:
    configs = load(json_file)
  return configs

def update_config(key='', value=False):
  if key in ['is_jsx', 'is_native']:
    configs = load_config()
    configs[key] = value
    with open('rcs.conf.json', 'w') as outfile:
      dump(configs, outfile)
