from pathlib import Path
from templates import component, index, styles, context
from load_config import load_config

ext = 'jsx' if load_config()['is_jsx'] else 'tsx'

def create_dir(dir_name='', super_dir=None):
  if not dir_name:
    raise Exception('cant find or create folder without dir_name')
  else:
    output_dir = None
    if super_dir:
      main_dir = Path('.') / f'{super_dir}'
      main_dir.mkdir(exist_ok=True)
      output_dir = main_dir / f'{dir_name.capitalize()}'
    else :
      output_dir = Path('.') / f'{dir_name.capitalize()}'
    output_dir.mkdir(exist_ok=True)
    return output_dir

def create_components(c_name='', dir_path=Path('.') / f'file', is_native=False):
  if not dir_path:
    raise Exception('failed to find a path to create components')
  else:
    component_filename = '%s.%s' % (c_name.capitalize(), ext)
    index_filename = 'index.%s' % (ext)
    styles_filename = '%s.styles.%s' % (c_name.capitalize(), ext)
    # ---
    component_path = dir_path / component_filename
    index_path = dir_path / index_filename
    styles_path = dir_path / styles_filename
    # ---
    with component_path.open("w", encoding="utf-8") as cff:
      cff.write(component(c_name))
    with index_path.open("w", encoding="utf-8") as iff:
      iff.write(index(c_name))
    with styles_path.open("w", encoding="utf-8") as sff:
      sff.write(styles(is_native))
  return component_path

def create_context(ctx_name='', dir_path=Path('.') / f'file'):
  if not dir_path:
    raise Exception('failed to find a path to create components')
  else:
    ctx_filename = '%sContext.%s' % (ctx_name.capitalize(), ext)
    ctx_path = dir_path / ctx_filename
    with ctx_path.open("w", encoding="utf-8") as ctxff:
      ctxff.write(context(ctx_name))
  return ctx_path
