#!/bin/python3
from time import sleep
from sys import argv
from utils import create_components, create_dir, create_context
from load_config import load_config

[ type, c_name, is_native, is_jsx ] = [ None, None, False, False ]
dir_path = None

if argv and len(argv) > 1:
  type = argv[1].lower()
  if type == 'help':
    print(
      'Welcome to React Styled Components CLI!!!\n'\
      '\n'\
      '- Commands availabel:\n'\
      '  "c" - generates a React Functional Component\n'\
      '  "p" - generates a React Functional Component with .page identifier\n'\
      '  "ctx" - generates a React context file\n'\
      '  "help" - print this message\n'\
      '\n'\
      '- All these commands (except "help") needs a "filename" param:\n'\
      '  example: \n'\
      '    $ rcs c home\n'\
      '  will generate:\n'\
      '    .\n'\
      '    |- components/\n'\
      '      |- index.tsx\n'\
      '      |- Home.tsx\n'\
      '      |- Home.styles.tsx\n'\
      '\n'\
      '- You can also provide an "-rn" flag at the and of command input.\n'\
      '  This option will generate the .styles file with "styled.Text``" instead of "styled.div``".\n'\
      '\n'\
      '- You can also run "rcs_config help" for more informations about changing defaults.'\
      '\n\n'\
      'https://github.com/erickvieira/react-styled-components-cli'
    )
  else:
    if len(argv) > 2:
      c_name = argv[2].lower()
    if len(argv) > 3:
      is_native = argv[3].lower() == '-rn'
    else:
      is_native = load_config()['is_native']
    if len(argv) > 4:
      is_jsx = argv[4].lower() == '-jsx'

    if not c_name:
      c_name = type
      print('Generating: %s component' % c_name)
    else:
      print('Generating: %s %s' % (c_name, { 'p': 'page', 'c': 'component', 'ctx': 'context' }[type]))

    def loading():
      dots = ['.' for i in range(0, 5) ]
      for dot in dots:
        sleep(0.2)
        print(dot)

    loading()

    final_path = None

    if type and type == 'p':
      dir_path = create_dir(c_name, 'pages')
      final_path = create_components('%s.page' % c_name, dir_path, is_native)
    elif type and type == 'c':
      dir_path = create_dir(c_name, 'components')
      final_path = create_components(c_name, dir_path, is_native)
    elif type and type == 'ctx':
      dir_path = create_dir('contexts')
      final_path = create_context(c_name, dir_path)
    else:
      dir_path = create_dir(c_name)
      final_path = create_components(c_name, dir_path)

    if final_path:
      print('%s was successful created!' % final_path)
    else:
      print('Sorry :(, a unhandled error occurred while creating your files.')
