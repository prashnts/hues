import hues

def test_sanity():
  assert type(hues.__version__) is tuple
  assert len(hues.__version__) == 3

def test_usage():
  # assert 'foo'.hues.red.bg_black == '\033[1;31;40mfoo\033[0m'
  pass
