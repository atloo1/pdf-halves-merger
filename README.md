# pdf-halves-merger
concatenate cropped halves of 2 single page PDFs into 1 PDF
```
 ________       ________        ________
|        |     |        |      |        |
|        |     |        |      |        |
|A      B|  +  |C      D|   →  |A      D|
|        |     |        |      |        |
|________|     |________|      |________|
```
OR
```
 ________       ________        ________
|   AA   |     |   CC   |      |   AA   |
|        |     |        |      |        |
|        |  +  |        |   →  |        |
|   BB   |     |   DD   |      |   DD   |
|________|     |________|      |________|
```
developed for combining 4x6 shipping labels into an 8.5x11 print

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
