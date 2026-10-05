# PDF to Anki Deck Converter

A lightweight Python CLI for turning standard PDF exports into Anki flashcards.

This project converts a page-based PDF into a ready-to-import Anki deck. Each page becomes one card: the front shows the page title, and the back includes the actual rendered page image from the original PDF.

## Features

- Converts a PDF into a deck with one card per page
- Extracts a clean title from each page
- Renders the original page graphic for the card back
- Exports a valid `.apkg` file for import into Anki
- Works well with standard, readable PDF exports such as iRealB output

## Scope

This project is intentionally focused on clean, structured PDFs rather than arbitrary scanned or malformed documents. It is optimized for reliability and simplicity over general-purpose PDF conversion.

## Installation

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/your-username/pdf-to-anki.git
cd pdf-to-anki
python -m pip install -e .
```

If you want to use the project virtual environment instead:

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

## Example

A 30-page PDF becomes a 30-card deck. Each card corresponds to one page, and the back of the card contains the actual page image so it remains visually faithful to the source document.

## Stack

- Python
- PyMuPDF
- genanki
- pytest

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.