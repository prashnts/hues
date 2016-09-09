'''Deterministic Push Down Automaton helpers.

This module implements helper functions to allow producing deterministic
representation of arbitrarily chained props.
'''
from functools import reduce


def zero_break(stack):
  '''Handle Resets in input stack.
  Breaks the input stack if a Reset operator (zero) is encountered.
  '''
  reducer = lambda x, y: tuple() if y == 0 else x + (y,)
  return reduce(reducer, stack, tuple())

def annihilate(stack, predicate):
  '''Squash and reduce the input stack.
  Removes the elements of input that match predicate and only keeps the last
  match at the beginning of stack.
  '''
  # Take the last matching element.
  n = next(filter(lambda x: x in predicate, stack[::-1]))
  # Take remaining elements.
  E = tuple(filter(lambda x: x not in predicate, stack))
  return (n,) + E

def dedup(stack):
  '''Remove duplicates from the stack in first-seen order.'''
  # Initializes with an accumulator and then reduces the stack with first match
  # deduplication.
  reducer = lambda x, y: x if y in x else x + (y,)
  return reduce(reducer, stack, tuple())
