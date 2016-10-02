from hues.colortable import FG, BG, HI_FG, HI_BG, STYLE, SEQ, KEYWORDS
# flake8: noqa

def test_foreground_colors():
  assert FG.black   == 30
  assert FG.red     == 31
  assert FG.green   == 32
  assert FG.yellow  == 33
  assert FG.blue    == 34
  assert FG.magenta == 35
  assert FG.cyan    == 36
  assert FG.white   == 37

def test_background_colors():
  assert BG.black   == 40
  assert BG.red     == 41
  assert BG.green   == 42
  assert BG.yellow  == 43
  assert BG.blue    == 44
  assert BG.magenta == 45
  assert BG.cyan    == 46
  assert BG.white   == 47

def test_bright_foreground_colors():
  assert HI_FG.black   == 90
  assert HI_FG.red     == 91
  assert HI_FG.green   == 92
  assert HI_FG.yellow  == 93
  assert HI_FG.blue    == 94
  assert HI_FG.magenta == 95
  assert HI_FG.cyan    == 96
  assert HI_FG.white   == 97

def test_bright_background_colors():
  assert HI_BG.black   == 100
  assert HI_BG.red     == 101
  assert HI_BG.green   == 102
  assert HI_BG.yellow  == 103
  assert HI_BG.blue    == 104
  assert HI_BG.magenta == 105
  assert HI_BG.cyan    == 106
  assert HI_BG.white   == 107

def test_ansi_styles():
  assert STYLE.reset     == 0
  assert STYLE.bold      == 1
  assert STYLE.italic    == 3
  assert STYLE.underline == 4
  assert STYLE.defaultfg == 39
  assert STYLE.defaultbg == 49

def test_sequence():
  assert SEQ % BG.black == '\033[40m'

def test_keywords():
  assert KEYWORDS.bg_black == BG.black
  assert KEYWORDS.bg_bright_black == HI_BG.black
  assert KEYWORDS.bold == STYLE.bold
