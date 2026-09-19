# PDF to Anki deck converter

A lightweight Python CLI for converting standard iRealB PDF exports into an Anki deck.

## Behavior
- Each PDF page becomes one Anki card
- The page title goes on the front of the card
- The full rendered page graphic goes on the back of the card
- The output is a valid `.apkg` deck file

## Usage

```bash
./.venv/bin/python main.py path/to/input.pdf --deck-name "My Deck"
```

This creates a file next to the PDF, for example:

```bash
path/to/input.apkg
```

## Scope
This tool is intentionally focused on the standard PDFs exported directly from iRealB. It is not a general-purpose PDF converter for arbitrary scanned or malformed PDFs.

## Stack
- Python
- PyMuPDF
- genanki
- pytest