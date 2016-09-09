import sys

from .colortable import KEYWORDS, SEQ


class BaseHues(str):
  '''Extend the string class to support hues.'''

  def __new__(cls, string, hue_stack=None):
    '''Return a new instance of the class.'''
    return super(BaseHues, cls).__new__(cls, string)

  def __init__(self, string, hue_stack=tuple()):
    self.string = string
    self._hue_stack = hue_stack

  def __getattr__(self, attr):
    try:
      code = getattr(KEYWORDS, attr)
      hues = self._hue_stack + (code,)
      return BaseHues(self.string, hue_stack=hues)
    except AttributeError as e:
      raise e

  def _apply_hues_(self):
    pass

  def __str__(self):
    pass
