import hues

def test_sanity():
  assert type(hues.__version__) is tuple
  assert len(hues.__version__) == 3
