# Math Teaching Tools

Experimental Python utilities for generating math teaching materials.

This repository is a cleaned-up basic version of a local prototype. It keeps
the reusable scripts and excludes generated slides, Word files, images, GIFs,
and installers.

## Tools

| Script | Purpose |
| --- | --- |
| `src/math_teaching_tools/latex_docx_to_markdown.py` | Extract paragraphs from a Word file and convert `latex:` lines into Markdown math blocks. |
| `src/math_teaching_tools/image_error_book.py` | Build a simple Word error book from a folder of problem images. |
| `src/math_teaching_tools/ppt_to_word.py` | Extract text from a PowerPoint file into a Word document. |
| `src/math_teaching_tools/sample_presentation.py` | Generate a small sample PowerPoint deck. |
| `src/math_teaching_tools/plot_3d_planes.py` | Show a small 3D math visualization demo. |
| `src/math_teaching_tools/problem_bank_index.py` | Build JSON/CSV indexes from converted problem-bank Markdown folders. |

## Install

```sh
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

`latex_docx_to_markdown.py` can optionally call Pandoc if you want to convert
the generated Markdown back into a Word file. Install Pandoc separately and
make sure `pandoc` is available in your terminal.

## Examples

Convert a Word file to Markdown math blocks:

```sh
python src/math_teaching_tools/latex_docx_to_markdown.py input.docx output/math_notes.md
```

Build an error book from images:

```sh
python src/math_teaching_tools/image_error_book.py problems output/error_book.docx
```

Extract PowerPoint text into Word:

```sh
python src/math_teaching_tools/ppt_to_word.py lesson.pptx output/lesson_notes.docx
```

Generate a sample deck:

```sh
python src/math_teaching_tools/sample_presentation.py output/sample_deck.pptx
```

Show the 3D plot demo:

```sh
python src/math_teaching_tools/plot_3d_planes.py
```

Index a converted problem-bank folder:

```sh
python src/math_teaching_tools/problem_bank_index.py converted_problem_bank output/problem_bank_index.json --csv-output output/problem_bank_index.csv
```

## Tutor Material Workflow

The intended workflow is:

1. Convert problem-bank PDFs into Markdown, metadata, and image folders.
2. Run `problem_bank_index.py` to create a searchable index.
3. Use the index to decide which problems belong in lesson notes, worksheets,
   error books, or `teaching.json` resources for a tutoring LINE bot.
4. Generate final teaching material with the Word, PowerPoint, and image tools
   in this repository.

## Project Status

Prototype. The scripts are useful for classroom workflow experiments, but they
are not a polished package yet.
