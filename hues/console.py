# Unicorns
'''Helper module for all the goodness.'''
import os
import sys
import yaml
from datetime import datetime

from .huestr import HueString
from .colortable import FG, BG, HI_FG, HI_BG, SEQ, STYLE, KEYWORDS

if sys.version_info.major == 2:
  str = unicode # noqa


CONFIG_FNAME = '.hues.yml'


class InvalidConfiguration(Exception):
  '''Raise when configuration is invalid.'''


class _Console(object):
  def __init__(self, stdout=sys.stdout):
    self.stdout = stdout
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

  def _base_log(self, *args, **kwargs):
    for arg in args:
      if not isinstance(arg, HueString):
        hue = getattr(FG, self.config['colors']['default'])
        arg = HueString(str(arg), hue_stack=(hue,))
      self.stdout.write(arg.colorized)
    if kwargs.get('newline', True):
      self.stdout.write('\n')


class SimpleConsole(_Console):
  info_label = 'I'
  warn_label = 'W'
  error_label = 'E'

  def log(self, *args):
    '''Generate a simple log string.
    Format: [{time}] - {messages}
    '''
    if self.config['showtime']:
      time = '[%s]' % datetime.now().strftime(self.config['timefmt'])
      args = self._labeled_log(time, 'time') + args
    self._base_log(*args)

  def _labeled_log(self, label, kind):
    '''Generate a labeled and colored log string.
    '''
    hue = getattr(FG, self.config['colors'][kind])
    return (HueString(label, hue_stack=(hue,)), ' - ')

  def info(self, *args):
    nargs = self._labeled_log(self.info_label, 'info') + args
    self.log(*nargs)

  def warn(self, *args):
    nargs = self._labeled_log(self.warn_label, 'warning') + args
    self.log(*nargs)

  def error(self, *args):
    nargs = self._labeled_log(self.error_label, 'error') + args
    self.log(*nargs)


class DefaultConsole(SimpleConsole):
  info_label = 'Info'
  warn_label = 'Warning'
  error_label = 'Error'


simple = SimpleConsole()
default = DefaultConsole()
