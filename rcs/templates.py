def component(name): 
  return 'import React from "react";\n'\
  'import { Container } from "./%s.styles";\n'\
  '\n'\
  'export default function() {\n'\
  '  return (\n'\
  '    <Container>\n'\
  '      %s is ready!\n'\
  '    </Container>\n'\
  '  );\n'\
  '}\n' % (name.capitalize(), name.capitalize())

def index(name): 
  return 'export { default } from "./%s";\n' % name.capitalize()

def styles(is_native=False): 
  from_path = '/native' if is_native else ''
  native_import = 'import { View } from "react-native";\n\n' if is_native else '\n'
  styled_element = 'View' if is_native else 'div'
  return 'import styled from "styled-components%s";\n'\
  '%s'\
  'export const Container = styled.%s`\n'\
  '  /* your styles go here */\n'\
  '`;\n' % (from_path, native_import, styled_element)

def context(name):
  n_cap = name.capitalize()
  return 'import React, { createContext, useState } from "react";\n'\
  '\n'\
  'interface %sContextProps {\n'\
  '  prop: any;\n'\
  '}\n'\
  '\n'\
  'const %sContext = createContext<%sContextProps>({ prop: null });\n'\
  '\n'\
  'export function %sProvider({ children }) {\n'\
  '  const [ prop ] = useState<any>(null);\n'\
  '\n'\
  '  return (\n'\
  '    <%sContext.Provider value={{ prop }}>\n'\
  '      { children }\n'\
  '    </%sContext.Provider>\n'\
  '  );\n'\
  '}\n'\
  'export const %sConsumer = %sContext.Consumer\n'\
  '\n'\
  'export default %sContext;\n' % (n_cap, n_cap, n_cap, n_cap, n_cap, n_cap, n_cap, n_cap, n_cap)