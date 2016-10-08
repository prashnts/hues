import sys
import collections

from hues.compat import string, UserString


def test_string_compat():
  if sys.version_info.major == 2:
    assert string is unicode  # noqa: F821
  else:
    assert string is str


def test_user_string():
  if hasattr(collections, 'UserString'):
    assert UserString is collections.UserString
  else:
    UserString('This is a test')
