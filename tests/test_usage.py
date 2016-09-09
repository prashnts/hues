import hues
from hues import hue

def test_sanity():
  assert type(hues.__version__) is tuple
  assert len(hues.__version__) == 3

def test_usage():
  assert str(hue('unicorn').red.bg_black) == '\033[31;40municorn\033[0m'

def test_chaining():
  p1 = hue(' here ').bg_blue
  p2 = hue('').blue
  assert hue.train(p1, p2) == '\033[44m here \033[0m\033[34m\033[0m'
