# PDF to Anki deck converter

A lightweight Python CLI for converting standard iRealB PDF exports into an Anki deck.

## Behavior
- Each PDF page becomes one Anki card
- The page title goes on the front of the card
- The full rendered page graphic goes on the back of the card
- The output is a valid `.apkg` deck file

## Install

From the project directory:

```bash
python -m pip install -e .
```

Or, if you want to use the local virtual environment:

```bash
./.venv/bin/python -m pip install -e .
```

## Usage

After installation, the CLI is available as:

```bash
pdf-to-anki path/to/input.pdf --deck-name "My Deck"
```

To overwrite an existing output file:

```bash
pdf-to-anki path/to/input.pdf --deck-name "My Deck" --overwrite
```

This creates a deck next to the PDF, for example:

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