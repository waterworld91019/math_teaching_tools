from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from docx import Document


def extract_latex_to_markdown(input_docx: Path, markdown_path: Path) -> None:
    document = Document(input_docx)
    lines: list[str] = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        if text.startswith("latex:"):
            latex_code = text.removeprefix("latex:").strip()
            lines.append(f"$$\n{latex_code}\n$$")
        elif text:
            lines.append(text)

    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text("\n\n".join(lines) + "\n", encoding="utf-8")


def convert_markdown_to_docx(markdown_path: Path, output_docx: Path) -> None:
    output_docx.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pandoc", str(markdown_path), "-o", str(output_docx)],
        check=True,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a Word file with 'latex:' paragraphs into Markdown math blocks.",
    )
    parser.add_argument("input_docx", type=Path)
    parser.add_argument("markdown_output", type=Path)
    parser.add_argument(
        "--docx-output",
        type=Path,
        help="Optional Word output path. Requires pandoc in PATH.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    extract_latex_to_markdown(args.input_docx, args.markdown_output)
    print(f"Wrote Markdown: {args.markdown_output}")

    if args.docx_output:
        convert_markdown_to_docx(args.markdown_output, args.docx_output)
        print(f"Wrote Word file: {args.docx_output}")


if __name__ == "__main__":
    main()
