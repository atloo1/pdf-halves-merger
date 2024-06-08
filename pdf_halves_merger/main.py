from pathlib import Path
from typing import Union

import click
import fitz  # PyMuPDF

BOTT = 'bottom'
L = 'left'
R = 'right'
TOP = 'top'
ALLOWED_HALVES = [BOTT, L, R, TOP]


def merge_pdf_halves(
    in_pdf_filepath_1: Union[Path, str],
    in_pdf_filepath_2: Union[Path, str],
    out_pdf_filepath: Union[Path, str] = 'merged.pdf',
    pdf_1_keep_half: str = L,
    pdf_2_keep_half: str = L,
):
    """
    concatenate cropped halves of 2 single page PDFs into 1 PDF

    run with:
    ```
    poetry run python -m pdf_halves_merger.main --help
    ```
    """
    # validate
    for pdf_keep_half in [pdf_1_keep_half, pdf_2_keep_half]:
        if pdf_keep_half not in ALLOWED_HALVES:
            raise ValueError(f'pdf_keep_half {pdf_keep_half} not in {ALLOWED_HALVES}')

    doc1 = fitz.open(in_pdf_filepath_1)
    doc2 = fitz.open(in_pdf_filepath_2)

    for doc in [doc1, doc2]:
        if len(doc) != 1:
            raise ValueError('input PDF not 1 page')

    rect1 = doc1[0].rect
    rect2 = doc2[0].rect

    if rect1 != rect2:
        raise ValueError('input PDF dimensions not identical')

    # define crop geometry
    doc_height = rect1.y1
    doc_width = rect1.x1
    bott_half = fitz.Rect(0, doc_height / 2, doc_width, doc_height)
    left_half = fitz.Rect(0, 0, doc_width / 2, doc_height)
    right_half = fitz.Rect(doc_width / 2, 0, doc_width, doc_height)
    top_half = fitz.Rect(0, 0, doc_width, doc_height / 2)

    # crop doc1
    if pdf_1_keep_half == BOTT:
        crop1 = bott_half
        position1 = top_half
    elif pdf_1_keep_half == L:
        crop1 = left_half
        position1 = left_half
    elif pdf_1_keep_half == R:
        crop1 = right_half
        position1 = left_half
    elif pdf_1_keep_half == TOP:
        crop1 = top_half
        position1 = top_half

    # crop doc2
    if pdf_2_keep_half == BOTT:
        crop2 = bott_half
        position2 = bott_half
    elif pdf_2_keep_half == L:
        crop2 = left_half
        position2 = right_half
    elif pdf_2_keep_half == R:
        crop2 = right_half
        position2 = right_half
    elif pdf_2_keep_half == TOP:
        crop2 = top_half
        position2 = bott_half

    # output
    output_doc = fitz.open()
    output_page = output_doc.new_page(width=doc_width, height=doc_height)
    output_page.show_pdf_page(position1, doc1, 0, clip=crop1)
    output_page.show_pdf_page(position2, doc2, 0, clip=crop2)
    output_doc.save(out_pdf_filepath)

    doc1.close()
    doc2.close()
    output_doc.close()


@click.command()
@click.option('--in-pdf-filepath-1', type=click.Path(exists=True))
@click.option('--in-pdf-filepath-2', type=click.Path(exists=True))
@click.option('--out-pdf-filepath', type=click.Path(), default='merged.pdf')
@click.option('--pdf-1-keep-half', default=L, type=str)
@click.option('--pdf-2-keep-half', default=L, type=str)
def _main(
    in_pdf_filepath_1: Union[Path, str],
    in_pdf_filepath_2: Union[Path, str],
    out_pdf_filepath: Union[Path, str],
    pdf_1_keep_half: str,
    pdf_2_keep_half: str,
):
    """private click CLI for merge_pdf_halves()"""
    merge_pdf_halves(
        in_pdf_filepath_1,
        in_pdf_filepath_2,
        out_pdf_filepath,
        pdf_1_keep_half,
        pdf_2_keep_half,
    )


if __name__ == '__main__':
    _main()
