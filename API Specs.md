# Hues Console

> Notes.

## API Considerations, Specs
Console API is borrowed from awesome Node.JS console api. [1]

```python
>>> from hues import console

>>> console.log
>>> console.error
>>> console.info
>>> console.warn
>>> console.assert
```

## Default color, theme settings
The default config is a JSON? YAML? file called .hues.[json/yml] in ~ or `cwd`.

## tqdm integration
We can ship with a tqdm wrapper.


[1]: https://nodejs.org/api/console.html
