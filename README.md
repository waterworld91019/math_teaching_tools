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

## Project Status

Prototype. The scripts are useful for classroom workflow experiments, but they
are not a polished package yet.
