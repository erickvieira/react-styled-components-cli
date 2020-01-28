from pathlib import Path
from templates import component, index, styles

def create_dir(dir_name=''):
  if not dir_name:
    raise Exception('cant find or create folder without dir_name')
  else:
    output_dir = Path('.') / f'{dir_name}'
    output_dir.mkdir(exist_ok=True)
    return output_dir

def create_components(c_name='', dir_path=Path('.') / f'file'):
  if not dir_path:
    raise Exception('failed to find a path to create components')
  else:
    component_filename = '%s.tsx' % c_name
    index_filename = 'index.tsx'
    styles_filename = '%s.styles.tsx' % c_name
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
      sff.write(styles())
