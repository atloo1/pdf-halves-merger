"""
test ../pdf_halves_merger/main.py

run with:
```
poetry run pytest tests/main_test.py
"""

import pytest

from pdf_halves_merger import main  # noqa: E999


def test_main():
    with pytest.raises(NotImplementedError):
        main.main()
