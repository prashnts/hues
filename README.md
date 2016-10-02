# Hues
This is the 90s and your terminal can display _16_ glorious colors. Your Python scripts deserve the some color love. `Hues` makes printing to console in color easy. Just grab the package from `PIP`, and your monochromatic days will be a thing of past!


## Quickstart

Go, grab the latest version from PIP. Run:

```bash
pip install hues
```

Then, in your scripts, do this:

```python
>>> import hues
>>> hues.log('42')
>>> hues.info('42')
```

### Configuration

[TODO]

_whoa!_

All the colors, styles and backgrounds are available as object attributes. The chainable syntax is optimized deterministically using a push down automaton, so when you're being particularly indecisive, you can:

```python
>>> print(hue('MONDAY!').bold.red.bg_green.underline.bright_yellow)
```

and there won't be a single trace of `red` in your `bright yellow` message to mondays.

Each `hue` string is self closing, so you can't accidentally color your whole terminal yellow because you forgot the `reset` escape sequence.


## Colors

All 16 glorious ANSI colors are available for both background and foreground. Assorted text styles such as **`bold`**, _`italics`_ and <u>`underline`</u> are also available. Too many colors? Worry not fam, go to town with `reset` attribute.


## Todo
- [ ] Expand this readme.
- [ ] Add screenshots!
- [ ] Unicorns required.

> Back in my days, we didn't even have colors!
