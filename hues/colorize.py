from functools import partial

from .colortable import FG, BG, HI_FG, HI_BG, SEQ, STYLE
from .dpda import zero_break, annihilator, dedup, apply

OPTIMIZATION_STEPS = (
  zero_break,               # Handle Resets using `reset`.
  annihilator(FG + HI_FG),  # Squash foreground colors to the last value.
  annihilator(BG + HI_BG),  # Squash background colors to the last value.
  dedup,                    # Remove duplicates in (remaining) style values.
)
optimize = partial(apply, OPTIMIZATION_STEPS)


def colorize(string, stack):
  '''Apply ANSI escape sequences to the string according to the stack.'''
  codes = optimize(stack)
  if len(codes):
    prefix = SEQ % ';'.join(map(str, codes))
    suffix = SEQ % STYLE.reset
    return prefix + string + suffix
  else:
    return string
