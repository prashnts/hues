import sys

if sys.version_info.major == 2:
  string = unicode # noqa
else:
  string = str

try:
  from collections import UserString
except ImportError:
  class UserString(string):
    def __new__(cls, seq, *args, **kwargs):
      return super(UserString, cls).__new__(cls, seq)
