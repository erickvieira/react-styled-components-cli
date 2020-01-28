#!/bin/python3
import sys
from utils import create_components, create_dir

[ c_name, modfier, mod_value ] = [ None, None, None ]

if sys.argv and len(sys.argv) > 1:
  c_name = sys.argv[1]
if len(sys.argv) > 2:
  modfier = sys.argv[2]
if len(sys.argv) > 3:
  mod_value = sys.argv[3]

print(c_name)

dir_path = create_dir(c_name)
create_components(c_name, dir_path)
