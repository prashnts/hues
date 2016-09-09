import sys

PY2 = int(sys.version[0]) == 2

if PY2:
  str = unicode


class BaseHues(str):
  '''Extend the string class to support hues.'''

  def __getattribute__(self, attr):
    if attr == 'hue':
      pass
    else:
      return super(BaseHues, self).__getattribute__(attr)
