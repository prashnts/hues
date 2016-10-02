# Unicorns
'''Helper module for all the goodness.'''
import os
import sys
import yaml
from datetime import datetime
from collections import namedtuple

from .huestr import HueString
from .colortable import KEYWORDS

if sys.version_info.major == 2:
  str = unicode # noqa


CONFIG_FNAME = '.hues.yml'


class InvalidConfiguration(Exception):
  '''Raise when configuration is invalid.'''


class _Console(object):
  def __init__(self, stdout=sys.stdout):
    self.stdout = stdout
    self.conf = self._resolve_config()

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

  def _resolve_config(self):
    '''Resolve configuration params to native instances'''
    conf = self._load_config()
    for k in conf['hues']:
      conf['hues'][k] = getattr(KEYWORDS, conf['hues'][k])
    hues = namedtuple('Hues', conf['hues'].keys())(**conf['hues'])
    opts = namedtuple('Options', conf['options'].keys())(**conf['options'])
    conf = namedtuple('HueConfig', ('hue', 'opts'))
    return conf(hues, opts)

  def _raw_log(self, *args):
    writeout = u''.join([x.colorized for x in args])
    self.stdout.write(writeout)
    if self.conf.opts.add_newline:
      self.stdout.write('\n')

  def getTime(self):
    return datetime.now().strftime(self.conf.opts.time_format)


class SimpleConsole(_Console):
  info_label = 'Info'
  warn_label = 'Warning'
  error_label = 'Error'

  def _base_log(self, contents, label=None, label_color=None):
    nargs = ()

    if self.conf.opts.show_time:
      timestr = '[{}]'.format(self.getTime())
      nargs += (
        HueString(timestr, hue_stack=(self.conf.hue.time,)),
        HueString(' - '),
      )

    if label:
      nargs += (
        HueString(label, hue_stack=(label_color,)),
        HueString(' - '),
      )

    content = u' '.join([str(x) for x in contents])
    nargs += (
      HueString(content, hue_stack=(self.conf.hue.default,)),
    )
    return self._raw_log(*nargs)

  def log(self, *args):
    return self._base_log(args)

  def info(self, *args):
    return self._base_log(args, self.info_label, self.conf.hue.info)

  def warn(self, *args):
    return self._base_log(args, self.warn_label, self.conf.hue.warning)

  def error(self, *args):
    return self._base_log(args, self.error_label, self.conf.hue.error)


simple = SimpleConsole()
