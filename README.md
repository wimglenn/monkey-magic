# Monkey Magic

Monkeypatch built-in types in Python.

### Installation

```bash
pip install monkey-magic
```

### Usage

```pycon
>>> def href(self):
...     return f'<a href="{self}">{self}</a>'
...
>>> from monkey_magic import monkeypatch
>>> monkeypatch(str, href)
>>> "www.example.com".href()
'<a href="www.example.com">www.example.com</a>'
```
