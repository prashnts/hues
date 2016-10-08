# Unicorns
import sys
from functools import partial
from collections import UserString

from .colortable import FG, BG, HI_FG, HI_BG, SEQ, STYLE, KEYWORDS, XFG_SEQ, XBG_SEQ
from .dpda import zero_break, annihilator, regxannihilator, dedup, apply
from .utils import hex_to_rgb

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


class HueString(UserString):
  '''Extend the string class to support hues.'''
  def __init__(self, seq, *hues, **kwhues):
    if 'fg' in kwhues:
      hues += (XFG_SEQ.format(*hex_to_rgb(kwhues['fg'])),)
    if 'bg' in kwhues:
      hues += (XBG_SEQ.format(*hex_to_rgb(kwhues['bg'])),)
    self.hues = hues
    self.data = seq

  def __getattr__(self, attr):
    try:
      code = getattr(KEYWORDS, attr)
      hues = self.hues + (code,)
      return HueString(self.data, *hues)
    except AttributeError as e:
      raise e

  @property
  def colorized(self):
    return colorize(self.data, self.hues)

  def __get_wrapped__(self, dat):
    return self.__class__(dat, *self.hues)

  def capitalize(self):
    return self.__get_wrapped__(self.data.capitalize())

  def casefold(self):
    return self.__get_wrapped__(self.data.casefold())

  def center(self, width, *args):
    return self.__get_wrapped__(self.data.center(width, *args))

  def expandtabs(self, tabsize=8):
    return self.__get_wrapped__(self.data.expandtabs(tabsize))

  def format(self, *args, **kwds):
    return self.__get_wrapped__(self.data.format(*args, **kwds))

  def format_map(self, mapping):
    return self.__get_wrapped__(self.data.format_map(mapping))

  def ljust(self, width, *args):
    return self.__get_wrapped__(self.data.ljust(width, *args))

  def lower(self):
    return self.__get_wrapped__(self.data.lower())

  def lstrip(self, chars=None):
    return self.__get_wrapped__(self.data.lstrip(chars))

  def partition(self, sep):
    return tuple(map(self.__get_wrapped__, self.data.partition(sep)))

  def replace(self, old, new, maxsplit=-1):
    return self.__get_wrapped__(self.data.replace(old, new, maxsplit))

  def rjust(self, width, *args):
    return self.__get_wrapped__(self.data.rjust(width, *args))

  def rpartition(self, sep):
    return tuple(map(self.__get_wrapped__, self.data.rpartition(sep)))

  def rstrip(self, chars=None):
    return self.__get_wrapped__(self.data.rstrip(chars))

  def split(self, sep=None, maxsplit=-1):
    return tuple(map(self.__get_wrapped__, self.data.split(sep, maxsplit)))

  def rsplit(self, sep=None, maxsplit=-1):
    return tuple(map(self.__get_wrapped__, self.data.rsplit(sep, maxsplit)))

  def splitlines(self, keepends=False):
    return tuple(map(self.__get_wrapped__, self.data.splitlines(keepends)))

  def strip(self, chars=None):
    return self.__get_wrapped__(self.data.strip(chars))

  def swapcase(self):
    return self.__get_wrapped__(self.data.swapcase())

  def title(self):
    return self.__get_wrapped__(self.data.title())

  def translate(self, *args):
    return self.__get_wrapped__(self.data.translate(*args))

  def upper(self):
    return self.__get_wrapped__(self.data.upper())

  def zfill(self, width):
    return self.__get_wrapped__(self.data.zfill(width))
