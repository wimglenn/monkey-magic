Monkey Magic
============

Monkeypatch built-in types in Python.

Installation
------------

.. code-block:: bash

   pip install monkey-magic

Usage
-----

Suppose you define a function ``href`` that you want to contribute as a "method" on ``str``:

.. code-block:: python

   def href(self: str) -> str:
       """make a url string into a hyperlink"""
       return f'<a href="{self}">{self}</a>'

Applying and then using it would look like this:

>>> from monkey_magic import monkeypatch
>>> monkeypatch(str, href)
>>> url = "www.example.com"
>>> url.href()
'<a href="www.example.com">www.example.com</a>'

This patch affects all strings, globally, including literals. It will work regardless of whether the patch was applied before or after a string instance was created.

.. skip: next

.. code-block::

   >>> help(str.href)
   Help on function href:

   href(self: str) -> str
      make a url string into a hyperlink


>>> "href" in dir(str)
True
>>> "hello".href
<bound method href of 'hello'>
>>> "hello".href()
'<a href="hello">hello</a>'


More Examples
-------------

Adding some pre-existing function:

>>> hi = """\
...     hello
...     world
... """
>>> import textwrap
>>> monkeypatch(str, textwrap.dedent)
>>> hi.dedent()
'hello\nworld\n'

Want to use a different name than the function's name?

.. code-block:: python

   import math

   def func(n):
       if n == 2 or n == 3:
           return True
       if n == 1 or n % 2 == 0:
           return False
       else:
           return all(n % i for i in range(3, int(1 + math.sqrt(n)), 2))

>>> monkeypatch(int, func, name="is_prime")
>>> 7 .is_prime()
True
>>> 8 .is_prime()
False

Contributing the unicode name function

>>> import unicodedata
>>> monkeypatch(str, unicodedata.name)
>>> "a".name()
'LATIN SMALL LETTER A'
>>> "💩".name()
'PILE OF POO'

Would you prefer that as a property instead of a method?

>>> monkeypatch(str, property(unicodedata.name), name="pname")
>>> "a".pname
'LATIN SMALL LETTER A'
>>> "🔥".pname
'FIRE'

To apply the same patch on a bunch of types:

.. code-block:: python

   @property
   def first(self):
       return next(iter(self))

>>> monkeypatch((str, bytes, tuple, list, dict), first)
>>> [1, 2].first
1
>>> (3, 4, 5).first
3
>>> "potato".first
'p'
>>> b"cafef00d".first
99
>>> {"k1": "v1", "k2": "v2"}.first
'k1'

Why does ``list.sort`` exist but ``dict.sort`` doesn't?

.. code-block:: python

   def sort(self, key=None, reverse=False):
       d_sort = {k: d[k] for k in sorted(self, key=key, reverse=reverse)}
       self.clear()
       self.update(d_sort)

>>> monkeypatch(dict, sort)
>>> d = {1: 1, 0: 0, 2: 2}
>>> d.sort()
>>> print(d)
{0: 0, 1: 1, 2: 2}
>>> d.sort(reverse=True)
>>> print(d)
{2: 2, 1: 1, 0: 0}
>>> d.sort(key=lambda k: k % 2)
>>> print(d)
{2: 2, 0: 0, 1: 1}

Just want an attribute, not a callable? That's fine.

>>> monkeypatch(list, 42, "number")
>>> [].number
42
>>> [1, 2].number
42


FAQ
---

... Why should I use this? Why not just use a function?
   You should not use this. Just use a function.

... Where are the tests?
   This ``README.rst`` is the test. The code-blocks in this document are actually `executed <https://github.com/simplistix/sybil>`_.

... Does this work in PyPy?
   The code uses implementation details of CPython. It will not work in PyPy.

... How to undo a patch?
   I don't know. When I try, Python segfaults. If you know how, `send me a PR <https://github.com/wimglenn/monkey-magic/pulls>`_.

... Did people really ask you these questions?
   Nope. I just made them up.
