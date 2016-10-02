# -*- coding: utf-8 -*-
import hues
from hues import huestr


def test_sanity():
  assert type(hues.__version__) is tuple
  assert len(hues.__version__) == 3


def test_usage():
  assert huestr('unicorn').red.bg_black.colorized == '\033[31;40municorn\033[0m'
