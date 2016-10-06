'''Implements helper utilities.'''
from collections import namedtuple

RGB = namedtuple('RGB', ('red', 'green', 'blue'))


def hex_to_rgb(color):
  '''Convert hex color string to a RGB tuple

  >>> hex_to_rgb('#FFF')
  RGB(red=255, green=255, blue=255)
  '''
  if not color.startswith('#') or len(color) not in (4, 7):
    raise ValueError('Expected a hex coded color value, got `{0}`'.format(color))

  hexcode = color[1:]
  if len(hexcode) == 3:
    hexcode = ''.join([x * 2 for x in hexcode])

  cvals = (int(hexcode[i * 2 : (i + 1) * 2], 16) for i in range(0, 3))
  return RGB(*cvals)
