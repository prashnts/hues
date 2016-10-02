# -*- coding: utf-8 -*-
# Unicorns
'''Helper module for all the goodness.'''
import os
import sys
import yaml
from datetime import datetime
from collections import namedtuple

from .huestr import HueString
from .colortable import KEYWORDS, FG

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
    as_tuples = lambda name, obj: namedtuple(name, obj.keys())(**obj)
    hues = as_tuples('Hues', conf['hues'])
    opts = as_tuples('Options', conf['options'])
    labels = as_tuples('Labels', conf['labels'])
    conf = namedtuple('HueConfig', ('hues', 'opts', 'labels'))
    return conf(hues, opts, labels)

  def _raw_log(self, *args):
    writeout = u''.join([x.colorized for x in args])
    self.stdout.write(writeout)
    if self.conf.opts.add_newline:
      self.stdout.write('\n')


class SimpleConsole(_Console):
  def _base_log(self, contents):
    def build_component(content, color=None):
      fg = KEYWORDS.defaultfg if color is None else color
      return (
        HueString(u'{}'.format(content), hue_stack=(fg,)),
        HueString(u' - '),
      )

    nargs = ()
    for content in contents:
      if type(content) is tuple and len(content) == 2:
        value, color = content
      else:
        value, color = content, None
      nargs += build_component(value, color)
    return self._raw_log(*nargs[:-1])

  def _getTime(self, wrap=None):
    time = datetime.now().strftime(self.conf.opts.time_format)
    return wrap.format(time) if wrap else time

  def log(self, *args, **kwargs):
    nargs = []
    if kwargs.get('time') or ('time' not in kwargs and self.conf.opts.show_time):
      nargs.append((self._getTime(), self.conf.hues.time))

    for k, v in kwargs.items():
      if k in ('info', 'warn', 'error', 'success'):
        if v:
          label = getattr(self.conf.labels, k)
          color = getattr(self.conf.hues, k)
          nargs.append((label, color))
    content = u' '.join([str(x) for x in args])
    nargs.append((content, self.conf.hues.default))
    return self._base_log(nargs)

  def info(self, *args):
    return self.log(*args, info=True)

  def warn(self, *args):
    return self.log(*args, warn=True)

  def error(self, *args):
    return self.log(*args, error=True)

  def success(self, *args):
    return self.log(*args, success=True)

  def __call__(self, *args):
    return self._base_log(args)


class Powerline(SimpleConsole):
  def _base_log(self, contents):
    def find_fg_color(bg):
      if bg >= 100:
        bg -= 70    # High intensity to regular intensity.
      if bg in (FG.green, FG.yellow, FG.white):
        return FG.black
      else:
        return FG.white

    def build_component(content, color=None, next_fg=None):
      fg = KEYWORDS.defaultfg if color is None else color
      text_bg = fg + 10  # Background Escape seq offsets by 10.
      text_fg = find_fg_color(fg)
      next_bg = KEYWORDS.defaultbg if next_fg is None else (next_fg + 10)

      return (
        HueString(u' {} '.format(content), hue_stack=(text_bg, text_fg)),
        HueString(u'', hue_stack=(fg, next_bg)),
      )

    nargs = ()

    for ix, content in enumerate(contents):
      try:
        next_fg = contents[ix + 1][1]
      except (IndexError, TypeError):
        next_fg = None
      if type(content) is tuple and len(content) == 2:
        value, color = content
      else:
        value, color = content, None
      nargs += build_component(value, color, next_fg)

    return self._raw_log(*nargs[:-1])
