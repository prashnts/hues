from hues.huestr import colorize
from hues.colortable import FG, BG, STYLE

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
