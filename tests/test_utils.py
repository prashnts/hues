from hues.utils import hex_to_rgb


def test_hex_to_rgb_usage():
  assert hex_to_rgb('#FFF') == (255, 255, 255)
  assert hex_to_rgb('#FFFFFF') == (255, 255, 255)
  assert hex_to_rgb('#2E2E2E') == (46, 46, 46)
  assert hex_to_rgb('#AABBBB') == (170, 187, 187)
  assert hex_to_rgb('#8B7E66') == (139, 126, 102)


def test_hex_to_rgb_exceptions():
  try:
    hex_to_rgb('TROLL!')
  except ValueError:
    pass

  try:
    hex_to_rgb('#TROLLL')
  except ValueError:
    pass
