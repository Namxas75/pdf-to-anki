# PDF to Anki CLI Build Plan

## Goal
Build a focused command-line tool for the standard PDFs exported directly from iRealB.

The initial scope is intentionally narrow:
- input: one standard iRealB PDF
- output: one `.apkg` Anki deck
- each page becomes one card
- front = page title
- back = full rendered page graphic
- no OCR
- no browser app
- no desktop app
- no mobile app
- no support for arbitrary PDFs outside the iRealB export format

## MVP definition
This is the target for v1:
- accept a single PDF file
- render each page to an image
- extract a reasonable title from the page text
- create one Anki note per page
- package the note images into a valid `.apkg`
- save the deck to disk

## Phase 1: Core CLI MVP
### Deliverables
- CLI entry point
- PDF input handling
- page-by-page rendering
- title extraction
- Anki deck export

### Tasks
1. Create the Python project skeleton
2. Install dependencies:
   - PyMuPDF for PDF rendering and text extraction
   - genanki for deck generation
   - pytest for validation
3. Implement `extract_page_title()`
4. Implement `render_page_image()`
5. Implement `build_notes_from_pdf()`
6. Implement `export_pdf_to_anki()`
7. Add CLI arguments:
   - input PDF path
   - optional output path
   - optional deck name
8. Validate that the generated `.apkg` is importable by Anki-compatible tools

## Phase 2: Validation and polish
### Deliverables
- reliable output for standard iRealB PDFs
- better title heuristics
- stronger test coverage

### Tasks
1. Add tests for title extraction on normal iRealB-style pages
2. Add tests for page count and deck structure
3. Ensure image files are included in package media
4. Improve error handling for missing files and malformed PDFs
5. Clean up CLI help and output messages

## Phase 3: Optional later improvements
These are explicitly out of scope for v1 and can be added later only if needed.

- OCR for scanned PDFs
- support for more arbitrary PDF layouts
- GUI desktop app
- web app
- iOS app
- advanced page-title detection using ML or document layout analysis

## Recommended stack
- Python
- PyMuPDF
- genanki
- pytest
- argparse

## Suggested milestone timeline
- Day 1: PDF parsing and page rendering
- Day 2: deck generation and media packaging
- Day 3: tests and CLI polish
- Day 4: validation with a real iRealB PDF

## Risks and limitations
- Scanned PDFs are out of scope for now
- Some iRealB exports may still have unusual layout edge cases
- Title extraction can be imperfect on pages without clear headings

## Success criteria
The MVP is successful when:
- a standard iRealB PDF converts to an `.apkg`
- each page becomes one card
- the card front contains a title
- the card back shows the actual page graphic
- the output deck imports into Anki or another Anki-compatible app

## Explicit scope boundary
This project is intentionally not a general-purpose PDF converter. It is a narrow tool for the standard PDF output produced by iRealB, and the first version should stay within that boundary.
