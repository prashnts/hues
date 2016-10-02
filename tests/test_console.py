import os
import pyfakefs.fake_filesystem_unittest as fake_fs_unittest

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

from hues.console import _Console, InvalidConfiguration # noqa


class Test_Console(fake_fs_unittest.TestCase):
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
    cs = _Console()
    assert cs.config['colors']['default'] == 'red'

  def test_local_config(self):
    os.chdir('/var/foo')
    cs = _Console()
    assert cs.config['colors']['default'] == 'green'

  def test_local_nested_config(self):
    os.chdir('/var/foo/bar/baz')
    cs = _Console()
    assert cs.config['colors']['default'] == 'green'

  def test_invalid_config(self):
    os.chdir('/var/invalid')
    with self.assertRaises(InvalidConfiguration) as e:
      _Console()
    assert 'not a dictionary' in str(e.exception)

  def test_invalid_yaml(self):
    os.chdir('/var/invalidyml')
    with self.assertRaises(InvalidConfiguration) as e:
      _Console()
    assert 'invalid YAML' in str(e.exception)
