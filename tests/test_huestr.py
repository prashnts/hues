import sys
from hues.huestr import colorize, HueString
from hues.colortable import FG, BG, STYLE


if sys.version_info.major == 2:
  str = unicode # noqa


def test_correct_colorization():
  expected = '\033[30;40municorns\033[0m'
  assert colorize('unicorns', (FG.black, BG.black)) == expected


def test_optimization():
  stack = (FG.black, FG.red, BG.green, STYLE.bold, STYLE.underline, BG.red)
  expected = '\033[1;4;31;41municorns\033[0m'
  assert colorize('unicorns', stack) == expected


def test_reset():
  stack = (FG.black, STYLE.reset)
  expected = 'unicorns'
  assert colorize('unicorns', stack) == expected


def test_reset_chained():
  stack = (FG.black, BG.black, STYLE.reset, FG.black)
  expected = '\033[30municorns\033[0m'
  assert colorize('unicorns', stack) == expected


def test_hues_creation():
  obj = HueString('woot')
  # assert isinstance(obj, str)
  assert obj.colorized == 'woot'


def test_hues_auto_stacking():
  obj = HueString('woot').cyan.bg_green
  # assert isinstance(obj, str)
  assert obj.hues == (FG.cyan, BG.green)


def test_hues_dynamic_props_exceptions():
  try:
    HueString('woot').noop
  except AttributeError as e:
    assert 'noop' in str(e)
  else:
    raise AssertionError


def test_hues_auto_colorize():
  obj = HueString('woot').cyan.bg_green
  assert obj.colorized == '\033[36;42mwoot\033[0m'
