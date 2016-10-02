# Unicorns
from .huestr import HueString as huestr
from .console import Config, SimpleConsole, PowerlineConsole

__version__ = (0, 2, 2)

conf = Config()

if conf.opts.theme == 'simple':
  console = SimpleConsole(conf=conf)
elif conf.opts.theme == 'powerline':
  console = PowerlineConsole(conf=conf)

log = console.log
info = console.info
warn = console.warn
error = console.error
success = console.success

del conf

__all__ = ('huestr', 'console', 'log', 'info', 'warn', 'error', 'success')
