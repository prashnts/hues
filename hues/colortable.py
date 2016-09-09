# Unicorns
'''Generate ANSI escape sequences for colors
Source: http://ascii-table.com/ansi-escape-sequences.php
'''
from collections import namedtuple

ANSIColors = namedtuple('ANSIColors', [
  'black', 'red', 'green', 'yellow',
  'blue', 'magenta', 'cyan', 'white',
])

# Style Codes
STYLE = namedtuple('ANSIStyles', [
  'reset', 'bold', 'italic', 'underline',
])(0, 1, 3, 4)

# Regular Colors
FG = ANSIColors(*range(30, 38))
BG = ANSIColors(*range(40, 48))

# High Intensity Colors
HI_FG = ANSIColors(*range(90, 98))
HI_BG = ANSIColors(*range(100, 108))

# Terminal sequence format
SEQ = '\033[%sm'
