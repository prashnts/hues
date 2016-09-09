import sys

from .colortable import FG, BG, HI_FG, HI_BG, STYLE, SEQ



class BaseHues(str):
  '''Extend the string class to support hues.'''
  def __init__(self, *args, **kwa):
    super(BaseHues, self).__init__(*args, **kwa)

  def __getattribute__(self, attr):
    if attr == 'hue':
      pass
    else:
      return super(BaseHues, self).__getattribute__(attr)

  def __str__(self):
    pass
