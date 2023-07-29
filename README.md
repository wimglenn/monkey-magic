# Monkey Magic

Monkeypatch built-in types in Python.

### Installation

```bash
pip install monkey-magic
```

### Usage

```pycon
>>> def href(s):
...     return '<a href="{0}">{0}</a>'.format(s)
...
>>> from monkey_magic import monkeypatch
>>> monkeypatch(str, href)
>>> "www.example.com".href()
'<a href="www.example.com">www.example.com</a>'
```
