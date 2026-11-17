import tempfile
from pathlib import Path

from pathos55cast_kit.core import Pathos55castTool


def test_count_basic():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "a.txt")
        path.write_text("one two\nthree\n", encoding="utf-8")
        stats = Pathos55castTool().count(path)
        assert stats == {"lines": 2, "words": 3, "chars": 14}


def test_missing_file_is_zeroed():
    assert Pathos55castTool().count("/no/such/file") == {"lines": 0, "words": 0, "chars": 0}


def test_total_sums():
    with tempfile.TemporaryDirectory() as tmp:
        a = Path(tmp, "a.txt"); a.write_text("x\n", encoding="utf-8")
        b = Path(tmp, "b.txt"); b.write_text("y z\n", encoding="utf-8")
        assert Pathos55castTool().total([a, b])["words"] == 3
