import textwrap
from unittest import TestCase

from monkey_magic import monkeypatch


def href(s):
    return '<a href="{0}">{0}</a>'.format(s)


class TestMonkey(TestCase):
    def setUp(self):
        monkeypatch(str, href)
        monkeypatch(str, textwrap.dedent)

    def test_href(self):
        actual = "example.org".href()
        expected = '<a href="example.org">example.org</a>'
        self.assertEqual(actual, expected)

    def test_dedent(self):
        actual = """\
            hello
            world
        """.dedent()
        expected = "hello\nworld\n"
        self.assertEqual(actual, expected)
