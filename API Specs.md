# Hues Console

> Notes.

## API Considerations, Specs
Console API is borrowed from awesome Node.JS console api. [1]

```python
>>> import hues

>>> hues.log('Look, mama!')   # No time, no leaders.
>>> hues.info('Stage 1', 'Operation started', level=0)   # Stage 1: Operation Started
>>> hues.info('Stage 1', 'Operation started', level=2)   # ----> Stage 1: Operation Started
>>> hues.warn('Uh, hello? Where are my memes?')
>>> hues.abort('I give up!')
>>> hues.error('Mann.', e)
```

## Default color, theme settings
The default config is a JSON? YAML? file called .hues.[json/yml] in ~ or `cwd`.

## tqdm integration
We can ship with a tqdm wrapper.


[1]: https://nodejs.org/api/console.html
