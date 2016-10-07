import hues.dpda as DPDA


def test_zero_negation():
  func = DPDA.zero_break
  assert func((1, 2, 3, 4, 0, 10, 1)) == (10, 1)
  assert func((1, 2, 3, 4, 5, 0)) == tuple()


def test_order_annihilation():
  func = DPDA._annihilate
  assert func(range(0, 10), (1, 2, 3, 4, 4, 3)) == (3,)
  assert func(range(5, 12), (1, 2, 10, 11, 11, 2)) == (1, 2, 2, 11)


def test_order_regex_annihilation():
  func = DPDA._annitilate_regex
  assert func('^foo', ('foobar', 'foobaz')) == ('foobaz',)
  assert func('^foo', ('foobar', 2, 3, 'foobaz')) == (2, 3, 'foobaz')


def test_built_order_annihilation():
  f1 = DPDA.annihilator(range(5, 12))
  assert f1((1, 2, 10, 11, 11, 2)) == (1, 2, 2, 11)


def test_built_order_regex_annihilation():
  f1 = DPDA.regxannihilator('^foo')
  assert f1(('foobar', 2, 3, 'foobaz')) == (2, 3, 'foobaz')


def test_dedup():
  func = DPDA.dedup
  assert func((1, 2, 3, 3, 4, 2, 1, 3, 5)) == (1, 2, 3, 4, 5)


def test_chaining():
  funcs = (
    DPDA.zero_break,                  # Take the last non-reset subset
    DPDA.annihilator(range(5)),       # Between 0 and 5, keep the last one
    DPDA.annihilator(range(10, 15)),  # Between 10 and 15, keep the last one
    DPDA.regxannihilator('^42;'),     # Test regexp matches of type `42;..` etc.
    DPDA.dedup,                       # Finally remove duplicates
  )
  stack = (1, 2, 3, 2, 2, 0, 1, 2, 3, '42;30', 2, 5, 5, 11, 3, 15, '42;@', 14)
  expected = (5, 15, 3, 14, '42;@')

  assert DPDA.apply(funcs, stack) == expected
  assert DPDA.apply(funcs, (1, 1, 0)) == tuple()
