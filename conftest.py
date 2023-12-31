from sybil import Sybil
from sybil.parsers.rest import DocTestParser, PythonCodeBlockParser, SkipParser

sybil = Sybil(
    parsers=[
        DocTestParser(),
        PythonCodeBlockParser(),
        SkipParser(),
    ],
    patterns=["*.rst"],
)
pytest_collect_file = sybil.pytest()
