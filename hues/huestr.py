# Unicorns
import sys
from functools import partial

from .colortable import FG, BG, HI_FG, HI_BG, SEQ, STYLE, KEYWORDS
from .dpda import zero_break, annihilator, dedup, apply

if sys.version_info.major == 2:
  # Python 2.7 compat.
  str = unicode


OPTIMIZATION_STEPS = (
  zero_break,               # Handle Resets using `reset`.
  annihilator(FG + HI_FG),  # Squash foreground colors to the last value.
  annihilator(BG + HI_BG),  # Squash background colors to the last value.
  dedup,                    # Remove duplicates in (remaining) style values.
)
optimize = partial(apply, OPTIMIZATION_STEPS)

def colorize(string, stack):
  '''Apply optimal ANSI escape sequences to the string.'''
  codes = optimize(stack)
  if len(codes):
    prefix = SEQ % ';'.join(map(str, codes))
    suffix = SEQ % STYLE.reset
    return prefix + string + suffix
  else:
    return string


class Hues(str):
  '''Extend the string class to support hues.'''
  def __new__(cls, string, hue_stack=None):
    '''Return a new instance of the class.'''
    return super(Hues, cls).__new__(cls, string)

  def __init__(self, string, hue_stack=tuple()):
    self.__string = string
    self.__hue_stack = hue_stack

  def __getattr__(self, attr):
    try:
      code = getattr(KEYWORDS, attr)
      hues = self.__hue_stack + (code,)
      return Hues(self.__string, hue_stack=hues)
    except AttributeError as e:
      raise e

  def __str__(self):
    return colorize(self.__string, self.__hue_stack)

  @staticmethod
  def train(*args):
    return ''.join(map(str, args))
