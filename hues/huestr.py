# Unicorns
import sys
from functools import partial

from .colortable import FG, BG, HI_FG, HI_BG, SEQ, STYLE, KEYWORDS
from .dpda import zero_break, annihilator, regxannihilator, dedup, apply

if sys.version_info.major == 2:
  str = unicode # noqa

XFG_REX = r'38;2;\d{1,3};\d{1,3};\d{1,3}'
XBG_REX = r'48;2;\d{1,3};\d{1,3};\d{1,3}'

OPTIMIZATION_STEPS = (
  zero_break,                 # Handle Resets using `reset`.
  annihilator(FG + HI_FG),    # Squash foreground colors to the last value.
  annihilator(BG + HI_BG),    # Squash background colors to the last value.
  regxannihilator(XFG_REX),   # Squash extended foreground
  regxannihilator(XBG_REX),   # Squash extended background
  dedup,                      # Remove duplicates in (remaining) style values.
)
optimize = partial(apply, OPTIMIZATION_STEPS)


def colorize(string, stack):
  '''Apply optimal ANSI escape sequences to the string.'''
  codes = optimize(stack)
  if len(codes):
    prefix = SEQ.format(';'.join(map(str, codes)))
    suffix = SEQ.format(STYLE.reset)
    return prefix + string + suffix
  else:
    return string


class HueString(str):
  '''Extend the string class to support hues.'''
  def __new__(cls, string, hue_stack=None):
    '''Return a new instance of the class.'''
    return super(HueString, cls).__new__(cls, string)

  def __init__(self, string, hue_stack=tuple()):
    self.__string = string
    self.__hue_stack = hue_stack

  def __getattr__(self, attr):
    try:
      code = getattr(KEYWORDS, attr)
      hues = self.__hue_stack + (code,)
      return HueString(self.__string, hue_stack=hues)
    except AttributeError as e:
      raise e

  @property
  def colorized(self):
    return colorize(self.__string, self.__hue_stack)


def xhuestring(str, fg=None, bg=None):
  pass
