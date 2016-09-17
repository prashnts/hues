# Unicorns
'''Helper module for all the goodness.'''
import os
import sys
import yaml

from .huestr import Hues

CONFIG_FNAME = '.hues.yml'


class InvalidConfiguration(Exception):
  '''Raise when configuration is invalid.'''


class _Console(object):
  def __init__(self, stdout=sys.stdout, stderr=sys.stderr):
    self.stdout = stdout
    self.stderr = stderr
    self.config = self._load_config()

  @staticmethod
  def _load_config():
    '''Find and load configuration params.
    Config files are loaded in the following order:
    - Beginning from current working dir, all the way to the root.
    - User home (~).
    - Module dir (defaults).
    '''
    def _load(cdir, recurse=False):
      confl = os.path.join(cdir, CONFIG_FNAME)
      try:
        with open(confl, 'r') as fp:
          conf = yaml.safe_load(fp)
          if type(conf) is not dict:
            raise InvalidConfiguration('Configuration at %s is not a dictionary.' % confl)
          return conf
      except EnvironmentError:
        parent = os.path.dirname(cdir)
        if recurse and parent != cdir:
          return _load(parent, recurse=True)
        else:
          return dict()
      except yaml.YAMLError:
        raise InvalidConfiguration('Configuration at %s is an invalid YAML file.' % confl)

    conf = _load(os.path.dirname(__file__))

    home_conf = _load(os.path.expanduser('~'))
    local_conf = _load(os.path.abspath(os.curdir), recurse=True)

    conf.update(home_conf)
    conf.update(local_conf)
    return conf
