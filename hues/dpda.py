# Unicorns
'''Deterministic Push Down Automaton helpers.

This module implements helper functions to allow producing deterministic
representation of arbitrarily chained props.
'''
from functools import reduce, partial


def zero_break(stack):
  '''Handle Resets in input stack.
  Breaks the input stack if a Reset operator (zero) is encountered.
  '''
  reducer = lambda x, y: tuple() if y == 0 else x + (y,)
  return reduce(reducer, stack, tuple())


def annihilate(predicate, stack):
  '''Squash and reduce the input stack.
  Removes the elements of input that match predicate and only keeps the last
  match at the end of the stack.
  '''
  extra = tuple(filter(lambda x: x not in predicate, stack))
  head = reduce(lambda x, y: y if y in predicate else x, stack, None)
  return extra + (head,) if head else extra


def annihilator(predicate):
  '''Build a partial annihilator for given predicate.'''
  return partial(annihilate, predicate)


def dedup(stack):
  '''Remove duplicates from the stack in first-seen order.'''
  # Initializes with an accumulator and then reduces the stack with first match
  # deduplication.
  reducer = lambda x, y: x if y in x else x + (y,)
  return reduce(reducer, stack, tuple())


def apply(funcs, stack):
  '''Apply functions to the stack, passing the resulting stack to next state.'''
  return reduce(lambda x, y: y(x), funcs, stack)


__all__ = ('zero_break', 'annihilator', 'dedup', 'apply')
