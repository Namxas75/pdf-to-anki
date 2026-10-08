# PDF to Anki Deck Converter

This tool is made for people using iRealB and wanting to turn a standard iRealB PDF export into an Anki deck.

Project links:
- GitHub: https://github.com/Namxas75/pdf-to-anki
- Issues: https://github.com/Namxas75/pdf-to-anki/issues

If you found this project on the iRealB forum, the workflow is simple:

1. Export a tune or setlist from iRealB as a PDF
2. Run this converter on that PDF
3. Import the generated `.apkg` file into Anki

Each page in the PDF becomes one Anki card. The front of the card shows a title extracted from the page, and the back shows the actual page image so the original chart remains visually faithful.

## Why this exists

This project was built for a practical use case: turning clean, readable iRealB PDFs into study cards for practice and memorization. It is intentionally focused on that workflow rather than trying to handle every possible PDF format or scanned document.

It works best with normal iRealB exports rather than badly formatted, low-quality, or scanned PDFs.

## Features

- Converts a PDF into a deck with one card per page
- Extracts a short, readable title from each page
- Uses the original PDF page image as the card back
- Exports a valid `.apkg` package for Anki import
- Works well with standard iRealB PDF output

## Installation

You need Python 3.9 or newer.

For the easiest setup, use the project helper script. It creates a local virtual environment and installs the dependencies for you.

### Option 1: easiest local setup

From the project folder:

```bash
./run.sh /path/to/irealb-export.pdf --deck-name "My iRealB Deck"
```

On Windows:

```bat
run.bat "C:\path\to\irealb-export.pdf" --deck-name "My iRealB Deck"
```

This handles the environment setup automatically, so you do not need to run Git, pip, or venv commands manually.

### Option 2: standard Python install

If you prefer the usual setup, clone the repository and install it in editable mode:

```bash
git clone https://github.com/Namxas75/pdf-to-anki.git
cd pdf-to-anki
python -m pip install -e .
```

If you already use a local virtual environment:

```bash
./.venv/bin/python -m pip install -e .
```

## Quick start

After installation, the CLI can be used directly:

```bash
pdf-to-anki /path/to/irealb-export.pdf --deck-name "My iRealB Deck"
```

Or, if you are using the helper script from the project folder:

```bash
./run.sh /path/to/irealb-export.pdf --deck-name "My iRealB Deck"
```

This creates an `.apkg` file next to the source PDF, so the workflow stays simple: export the PDF from iRealB, run the tool, import the deck into Anki.

For example, if your file is:

```bash
/Users/you/Desktop/irealb-export.pdf
```

it will generate:

```bash
/Users/you/Desktop/irealb-export.apkg
```

You can then open Anki and import the deck from that file.

## Overwrite an existing deck

If the output file already exists:

```bash
pdf-to-anki /path/to/irealb-export.pdf --deck-name "My iRealB Deck" --overwrite
```

## Custom output path

You can also choose a specific output filename:

```bash
pdf-to-anki /path/to/irealb-export.pdf -o /path/to/my-deck.apkg --deck-name "Jazz Standards"
```

## Example workflow

A 30-page iRealB export becomes a 30-card deck. Each card corresponds to one page, and the back of each card contains the original page image, which makes the deck useful for visual reference while studying.

## Notes for iRealB users

- This is meant for clean PDF exports from iRealB
- It is not a full OCR or document-conversion tool
- The project is intentionally simple and reliable for the common iRealB use case
- It is best suited for practice decks built from standard lead sheets and chart PDFs

## Stack

- Python
- PyMuPDF
- genanki
- pytest

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.