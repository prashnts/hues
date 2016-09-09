import hues.dpda as dpda


def test_zero_negation():
  # Identity function for future tests.
  reduce = lambda x: x
  assert reduce((1, 2, 3, 4, 0, 10, 1)) == (10, 1)
  assert reduce((1, 2, 3, 4, 5, 0)) == (0,)
