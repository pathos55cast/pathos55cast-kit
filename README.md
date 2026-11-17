# pathos55cast-kit

Count lines, words and characters, with totals.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m pathos55cast_kit.cli --help
```

```python
from pathos55cast_kit.core import Pathos55castTool

tool = Pathos55castTool()
print(tool)
```

## Layout

```
pathos55cast_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 pathos55cast
