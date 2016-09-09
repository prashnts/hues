import hues.dpda as DPDA

reduce = lambda x: x

def test_zero_negation():
  func = DPDA.zero_break
  assert func((1, 2, 3, 4, 0, 10, 1)) == (10, 1)
  assert func((1, 2, 3, 4, 5, 0)) == tuple()

def test_order_annihilation():
  func = DPDA.annihilate
  assert func((1, 2, 3, 4, 4, 3), range(0, 10)) == (3,)
  assert func((1, 2, 10, 11, 11, 2), range(5, 12)) == (11, 1, 2, 2)

def test_dedup():
  func = DPDA.dedup
  assert func((1, 2, 3, 3, 4, 2, 1, 3, 5)) == (1, 2, 3, 4, 5)
