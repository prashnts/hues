import os
import pyfakefs.fake_filesystem_unittest as fake_fs_unittest

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock # noqa

CONFIG_FNAME = '.hues.yml'
usr_conf = os.path.join(os.path.expanduser('~'), CONFIG_FNAME)
mod_conf = os.path.join(os.path.dirname(__file__), '..', 'hues', CONFIG_FNAME)

with open(mod_conf, 'r') as fp:
  default_conf = fp.read()

home_conf = '''
colors:
  default: red
'''
local_conf = '''
colors:
  default: green
'''
invalid_conf = '''Invalid Conf, but valid YAML.'''
invalid_yaml = '''Nested: Dicts: Are: Invalid!'''

from hues.console import (
  Config,
  InvalidConfiguration,
  SimpleConsole,
  PowerlineConsole) # noqa


class Test_Config(fake_fs_unittest.TestCase):
  def setUp(self):
    self.setUpPyfakefs()
    self.fs.CreateFile(mod_conf, contents=default_conf)
    self.fs.CreateFile(usr_conf, contents=home_conf)
    self.fs.CreateFile('/var/foo/.hues.yml', contents=local_conf)
    self.fs.CreateFile('/var/invalid/.hues.yml', contents=invalid_conf)
    self.fs.CreateFile('/var/invalidyml/.hues.yml', contents=invalid_yaml)
    self.fs.CreateDirectory('/var/foo/bar/baz')
    self.fs.CreateDirectory('/var/doom/baz')

  def test_home_config(self):
    os.chdir('/var/doom/baz')
    cs = Config.load_config()
    assert cs['colors']['default'] == 'red'

  def test_local_config(self):
    os.chdir('/var/foo')
    cs = Config.load_config()
    assert cs['colors']['default'] == 'green'

  def test_local_nested_config(self):
    os.chdir('/var/foo/bar/baz')
    cs = Config.load_config()
    assert cs['colors']['default'] == 'green'

  def test_invalid_config(self):
    os.chdir('/var/invalid')
    with self.assertRaises(InvalidConfiguration) as e:
      Config.load_config()
    assert 'not a dictionary' in str(e.exception)

  def test_invalid_yaml(self):
    os.chdir('/var/invalidyml')
    with self.assertRaises(InvalidConfiguration) as e:
      Config.load_config()
    assert 'invalid YAML' in str(e.exception)


def test_resolved_config():
  cs = Config()
  assert hasattr(cs, 'hues')
  assert hasattr(cs, 'opts')
  assert hasattr(cs.hues, 'default')


def test_simple_console():
  console = SimpleConsole(conf=Config())
  for func in ('log', 'info', 'warn', 'error', 'success'):
    assert hasattr(console, func)


def _get_mock_stdout():
  stdout = Mock()
  write = Mock(return_value=None)
  stdout.attach_mock(write, 'write')
  return stdout, write


def test_raw_log_write():
  stdout, write = _get_mock_stdout()
  console = SimpleConsole(conf=Config(), stdout=stdout)
  console.log('foo')
  assert write.call_count == 2
  write.assert_any_call('\n')

  assertions = []
  for call in write.mock_calls:
    assertions.append(call.called_with.endswith('\033[39mfoo\033[0m'))
  assert any(assertions)


def test_helpers():
  stdout, write = _get_mock_stdout()
  console = SimpleConsole(conf=Config(), stdout=stdout)
  predicate = lambda a, b: lambda x: a in x and b in x
  anymatch = lambda colln, predicate: any([predicate(c) for c in colln])
  callargs = lambda x: [str(x) for x in x]

  assert predicate('a', 'b')('oh, hello! we have b.')
  assert anymatch(['foo', 'bar'], predicate('ba', 'ar'))

  console.info('alpha')
  assert anymatch(callargs(write.mock_calls), predicate('INFO', 'alpha'))
  console.error('beta')
  assert anymatch(callargs(write.mock_calls), predicate('ERROR', 'beta'))
  console.warn('delta')
  assert anymatch(callargs(write.mock_calls), predicate('WARN', 'delta'))
  console.success('pi')
  assert anymatch(callargs(write.mock_calls), predicate('SUCCESS', 'pi'))

  console(('Hey', 30), ('You', 31))
  assert anymatch(callargs(write.mock_calls), predicate('Hey', 'You'))


def test_default_color():
  stdout, write = _get_mock_stdout()
  console = SimpleConsole(conf=Config(), stdout=stdout)
  console('foo')
  write.assert_any_call('\033[39mfoo\033[0m')


def test_powerline():
  stdout, write = _get_mock_stdout()
  console = PowerlineConsole(conf=Config(), stdout=stdout)
  console.log('foo', time=False)
  write.assert_any_call('\033[49;37m foo \033[0m')
  console(('foo', 92), ('bar', 92), 'baz')
