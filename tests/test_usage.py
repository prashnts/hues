# -*- coding: utf-8 -*-
import hues
from hues import hue


def test_sanity():
  assert type(hues.__version__) is tuple
  assert len(hues.__version__) == 3


def test_usage():
  assert hue('unicorn').red.bg_black.colorized == '\033[31;40municorn\033[0m'
