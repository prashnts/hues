import hues.colortable as colortable


def test_foreground_colors():
  FG = colortable.FG
  assert FG.black   == 30
  assert FG.red     == 31
  assert FG.green   == 32
  assert FG.yellow  == 33
  assert FG.blue    == 34
  assert FG.magenta == 35
  assert FG.cyan    == 36
  assert FG.white   == 37

def test_background_colors():
  BG = colortable.BG
  assert BG.black   == 40
  assert BG.red     == 41
  assert BG.green   == 42
  assert BG.yellow  == 43
  assert BG.blue    == 44
  assert BG.magenta == 45
  assert BG.cyan    == 46
  assert BG.white   == 47

def test_bright_foreground_colors():
  HI_FG = colortable.HI_FG
  assert HI_FG.black   == 90
  assert HI_FG.red     == 91
  assert HI_FG.green   == 92
  assert HI_FG.yellow  == 93
  assert HI_FG.blue    == 94
  assert HI_FG.magenta == 95
  assert HI_FG.cyan    == 96
  assert HI_FG.white   == 97

def test_bright_background_colors():
  HI_BG = colortable.HI_BG
  assert HI_BG.black   == 100
  assert HI_BG.red     == 101
  assert HI_BG.green   == 102
  assert HI_BG.yellow  == 103
  assert HI_BG.blue    == 104
  assert HI_BG.magenta == 105
  assert HI_BG.cyan    == 106
  assert HI_BG.white   == 107

def test_ansi_styles():
  STYL = colortable.STYLE
  assert STYL.reset     == 0
  assert STYL.bold      == 1
  assert STYL.italic    == 3
  assert STYL.underline == 4

def test_sequence():
  SEQ = colortable.SEQ
  assert SEQ % colortable.BG.black == '\033[40m'
