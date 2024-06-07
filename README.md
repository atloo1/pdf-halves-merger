# pdf-halves-merger
2 halves of 1 page PDFs → 1 PDF

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
### first time setup
```
pyenv install 3.9 --skip-existing   # or your choice
pyenv local 3.9   # or your choice
poetry install
poetry run pre-commit install
```
### test locally (preemptively pass the corresponding GitHub action)
`poetry run pytest`
