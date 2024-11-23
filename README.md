# pdf-halves-merger

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/atloo1/pdf-halves-merger/ci.yaml)](https://github.com/atloo1/pdf-halves-merger/actions/workflows/ci.yaml?query=branch%3Amain)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Fpdf-halves-merger%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.dependencies.python&label=python)](https://github.com/atloo1/pdf-halves-merger/blob/main/pyproject.toml)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Fpdf-halves-merger%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.version&label=version)](https://github.com/atloo1/pdf-halves-merger/blob/main/pyproject.toml)
[![GitHub License](https://img.shields.io/github/license/atloo1/pdf-halves-merger)](https://github.com/atloo1/pdf-halves-merger/blob/main/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/atloo1/pdf-halves-merger)

[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

concatenate cropped halves of 2 single page PDFs into 1 PDF:

```
┌─────────┐       ┌─────────┐       ┌─────────┐
│         │       │         │       │         │
│         │       │         │       │         │
│ A     B │   +   │ C     D │   →   │ A     D │
│         │       │         │       │         │
│         │       │         │       │         │
└─────────┘       └─────────┘       └─────────┘

```

OR

```
┌─────────┐       ┌─────────┐       ┌─────────┐
│    A    │       │    C    │       │    A    │
│         │       │         │       │         │
│         │   +   │         │   →   │         │
│         │       │         │       │         │
│    B    │       │    D    │       │    D    │
└─────────┘       └─────────┘       └─────────┘

```

motivated by wanting 2 4x6 inch shipping labels on 1 8.5x11 inch print

## prerequisites

- [poetry](https://python-poetry.org/docs/#installing-with-pipx)

```
git clone https://github.com/atloo1/pdf-halves-merger.git
cd pdf-halves-merger/
```

## run

```
poetry install --without dev
poetry run python -m pdf_halves_merger.main --help
```

## develop

### prerequisites

- [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

### 1st time setup

```
pyenv install 3.9 --skip-existing   # or your choice
pyenv local 3.9   # or your choice
poetry install
poetry run pre-commit install
```
