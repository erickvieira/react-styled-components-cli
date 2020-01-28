from sys import argv
from load_config import load_config, update_config

[ command, variable ] = [ None, None ]

if argv and len(argv) > 1:
  command = argv[1].lower()
if len(argv) > 2:
  variable = argv[2].lower()

if command not in ['use', 'help']:
  print('%s is not a known command. Use "rcs_config help" for details.' % command)
else:
  if command == 'help':
    print(
      'Welcome to React Styled Components CLI Configs!!!\n'\
      '\n'\
      '- Commands availabel:\n'\
      '  "use" - changes one of the CLI default configurations.\n'\
      '  "help" - print this message\n'\
      '\n'\
      '- The "use" command needs a "variable" param:\n'\
      '  example: \n'\
      '    $ rcs_config use reactjs\n'\
      '  will setup the CLI to allways generates ReactJS components instead of React Native ones.\n'\
      '\n'\
      '- The default configuration is:\n'\
      '  {\n'\
      '    "is_native": false,\n'\
      '    "is_jsx": false,\n'\
      '  }\n'\
      '\n'\
      '- The available use commands are:\n'\
      '  "react-native" - set the "is_native" to true\n'\
      '  "reactjs" - set the "is_native" to false\n'\
      '  "jsx" - set the "is_jsx" to true\n'\
      '  "tsx" - set the "is_jsx" to false\n'\
      '\n'\
      '- You can also run "rcs help" for more informations about CLI commands.'\
      '\n\n'\
      'https://github.com/erickvieira/react-styled-components-cli'
    )
  else:
    variables = ['react-native', 'reactjs', 'jsx', 'tsx']
    if variable not in variables:
      print('%s is not a known variable. Use "rcs_config help" for details.' % variable)
    else:
      if variable in ['react-native', 'reactjs']:
        update_config('is_native', variable == 'react-native')
      elif variable in ['jsx', 'tsx']:
        update_config('is_jsx', variable == 'jsx')