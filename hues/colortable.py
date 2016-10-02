# Unicorns
'''Generate ANSI escape sequences for colors
Source: http://ascii-table.com/ansi-escape-sequences.php
'''
from collections import namedtuple

ANSIColors = namedtuple('ANSIColors', [
  'black', 'red', 'green', 'yellow',
  'blue', 'magenta', 'cyan', 'white',
])
ANSIStyles = namedtuple('ANSIStyles', [
  'reset', 'bold', 'italic', 'underline', 'defaultfg', 'defaultbg',
])

# Style Codes
STYLE = ANSIStyles(0, 1, 3, 4, 39, 49)

# Regular Colors
FG = ANSIColors(*range(30, 38))
BG = ANSIColors(*range(40, 48))

# High Intensity Colors
HI_FG = ANSIColors(*range(90, 98))
HI_BG = ANSIColors(*range(100, 108))

# Terminal sequence format
SEQ = '\033[%sm'


def __gen_keywords__(*args, **kwargs):
  '''Helper function to generate single escape sequence mapping.'''
  fields = tuple()
  values = tuple()

  for tpl in args:
    fields += tpl._fields
    values += tpl
  for prefix, tpl in kwargs.items():
    fields += tuple(map(lambda x: '_'.join([prefix, x]), tpl._fields))
    values += tpl

  return namedtuple('ANSISequences', fields)(*values)

KEYWORDS = __gen_keywords__(STYLE, FG, bg=BG, bright=HI_FG, bg_bright=HI_BG)
