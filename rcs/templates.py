def component(name): 
  return 'import React from "react";\n'\
  'import { Container } from "./%s.styles";\n'\
  '\n'\
  'export default function() {\n'\
  '  return (\n'\
  '    <Container>Hello</Container>\n'\
  '  );\n'\
  '}\n' % name

def index(name): 
  return 'export { default } from "./%s";\n' % name

def styles(): 
  return 'import styled from "styled-components";\n'\
  '\n'\
  'const Container = styled.button`\n'\
  '  /* your styles go here */\n'\
  '`;\n'
