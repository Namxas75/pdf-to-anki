import shutil

import pytest

from pdf_to_anki import extract_page_title, build_notes_from_pdf, export_pdf_to_anki, make_deck


def test_extract_page_title_prefers_heading_like_line():
    page_text = "\n".join([
        "Introduction",
        "Some explanatory text here.",
        "Another line with more information.",
    ])

    assert extract_page_title(page_text) == "Introduction"


def test_extract_page_title_falls_back_to_first_non_empty_line():
    page_text = "\n".join([
        "          ",
        "Chapter 1",
        "This is body text.",
    ])

    assert extract_page_title(page_text) == "Chapter 1"


def test_build_notes_from_pdf_creates_card_per_page():
    notes = build_notes_from_pdf("tests/fixtures/simple.pdf")

    assert len(notes) == 2
    assert notes[0]["front"] == "First page"
    assert "<img" in notes[0]["back"]
    assert notes[1]["front"] == "Second page"
    assert "<img" in notes[1]["back"]


def test_make_deck_uses_pdf_title_as_deck_name():
    deck = make_deck("tests/fixtures/simple.pdf", "PDF Deck")

    assert deck.name == "PDF Deck"


def test_export_pdf_to_anki_refuses_to_overwrite_without_permission(tmp_path):
    source = tmp_path / "source.pdf"
    shutil.copy("tests/fixtures/simple.pdf", source)
    output = tmp_path / "source.apkg"
    output.write_bytes(b"existing")

    with pytest.raises(FileExistsError):
        export_pdf_to_anki(str(source), str(output))
