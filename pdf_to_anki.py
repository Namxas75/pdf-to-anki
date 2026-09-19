from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

import fitz
import genanki


def ensure_output_path_available(output_path: Path, overwrite: bool = False) -> None:
    if output_path.exists() and not overwrite:
        raise FileExistsError(
            f"Output file already exists: {output_path}. Use --overwrite to replace it."
        )


def normalize_text(value: str) -> str:
    return " ".join(value.strip().split())


def extract_page_title(page_text: str) -> str:
    if not page_text:
        return "Untitled Page"

    lines = [normalize_text(line) for line in page_text.splitlines() if line.strip()]
    if not lines:
        return "Untitled Page"

    for line in lines[:10]:
        word_count = len(line.split())
        if 1 <= len(line) <= 120 and word_count <= 12:
            return line

    for line in lines:
        if line:
            return line

    return "Untitled Page"


def render_page_image(doc: fitz.Document, page_number: int, output_dir: Path) -> str:
    page = doc[page_number]
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    image_name = f"page_{page_number + 1:03d}.png"
    image_path = output_dir / image_name
    pix.save(str(image_path))
    return image_name


def build_notes_from_pdf(pdf_path: str, media_dir: str | None = None) -> List[Dict[str, str]]:
    doc = fitz.open(pdf_path)
    output_dir = Path(media_dir) if media_dir else Path(pdf_path).resolve().parent / ".anki_media"
    output_dir.mkdir(parents=True, exist_ok=True)

    notes: List[Dict[str, str]] = []
    for page_number in range(len(doc)):
        page_text = doc[page_number].get_text("text").strip()
        title = extract_page_title(page_text)
        image_name = render_page_image(doc, page_number, output_dir)
        notes.append({
            "front": title,
            "back": f'<img src="{image_name}" alt="{title}" />',
            "image": str(output_dir / image_name),
        })

    doc.close()
    return notes


def make_deck(pdf_path: str, deck_name: str = "PDF Deck") -> genanki.Deck:
    deck_id = 2024091901
    model_id = 2024091902

    model = genanki.Model(
        model_id,
        "PDF Page Card",
        fields=[{"name": "Front"}, {"name": "Back"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Front}}",
                "afmt": "{{Front}}<hr id='answer'>{{Back}}",
            }
        ],
    )

    deck = genanki.Deck(deck_id, deck_name)
    media_dir = Path(pdf_path).resolve().parent / ".anki_media"

    for note_data in build_notes_from_pdf(pdf_path, str(media_dir)):
        note = genanki.Note(model=model, fields=[note_data["front"], note_data["back"]])
        deck.add_note(note)

    return deck


def export_pdf_to_anki(
    pdf_path: str,
    output_path: str | None = None,
    deck_name: str | None = None,
    overwrite: bool = False,
) -> str:
    source_path = Path(pdf_path)
    if output_path is None:
        output_path = str(source_path.with_suffix(".apkg"))

    destination = Path(output_path)
    ensure_output_path_available(destination, overwrite)

    deck = make_deck(str(source_path), deck_name or source_path.stem or "PDF Deck")
    package = genanki.Package(deck)
    media_dir = source_path.parent / ".anki_media"
    package.media_files = [str(path) for path in sorted(media_dir.glob("*.png"))]
    package.write_to_file(str(destination))
    return str(destination)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a standard iRealB PDF into an Anki deck with one card per page.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("pdf_path", help="Path to the source PDF file")
    parser.add_argument("-o", "--output", help="Destination .apkg path")
    parser.add_argument("--deck-name", help="Name of the Anki deck to create")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the destination file if it already exists.",
    )
    args = parser.parse_args()

    output = export_pdf_to_anki(args.pdf_path, args.output, args.deck_name, args.overwrite)
    print(f"Created Anki deck: {output}")


if __name__ == "__main__":
    main()
