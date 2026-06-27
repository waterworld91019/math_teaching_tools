from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    return json.loads(path.read_text(encoding="utf-8"))


def first_heading(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or fallback

    return fallback


def preview_text(markdown_text: str, max_chars: int) -> str:
    lines = []
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("!["):
            continue
        if set(stripped) <= {"-", "|", " "}:
            continue
        lines.append(stripped)

    preview = " ".join(lines)
    return preview[:max_chars]


def find_meta_path(markdown_path: Path) -> Path | None:
    candidates = [
        markdown_path.with_name(f"{markdown_path.stem}_meta.json"),
        markdown_path.with_suffix(".json"),
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return None


def collect_image_count(folder: Path) -> int:
    return sum(
        1
        for path in folder.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )


def build_record(input_root: Path, markdown_path: Path, max_preview_chars: int) -> dict[str, Any]:
    markdown_text = markdown_path.read_text(encoding="utf-8", errors="replace")
    meta_path = find_meta_path(markdown_path)
    meta = load_json(meta_path) if meta_path else {}
    ocr_stats = meta.get("ocr_stats", {})
    block_stats = meta.get("block_stats", {})
    equation_stats = block_stats.get("equations", {})

    return {
        "id": markdown_path.stem,
        "title": first_heading(markdown_text, markdown_path.stem),
        "source_dir": str(markdown_path.parent.relative_to(input_root)),
        "markdown_path": str(markdown_path.relative_to(input_root)),
        "meta_path": str(meta_path.relative_to(input_root)) if meta_path else "",
        "pages": meta.get("pages", 0),
        "ocr_engine": ocr_stats.get("ocr_engine", ""),
        "ocr_success": ocr_stats.get("ocr_success", 0),
        "ocr_failed": ocr_stats.get("ocr_failed", 0),
        "table_count": block_stats.get("table", 0),
        "equation_count": equation_stats.get("equations", 0),
        "image_count": collect_image_count(markdown_path.parent),
        "preview": preview_text(markdown_text, max_preview_chars),
    }


def build_problem_bank_index(input_root: Path, max_preview_chars: int) -> list[dict[str, Any]]:
    markdown_files = sorted(
        path
        for path in input_root.rglob("*.md")
        if path.is_file() and not path.name.startswith(".")
    )

    return [
        build_record(input_root, markdown_path, max_preview_chars)
        for markdown_path in markdown_files
    ]


def write_json(records: list[dict[str, Any]], output_path: Path) -> None:
    payload = {
        "version": "1.0.0",
        "document_count": len(records),
        "documents": records,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_csv(records: list[dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id",
        "title",
        "source_dir",
        "markdown_path",
        "meta_path",
        "pages",
        "ocr_engine",
        "ocr_success",
        "ocr_failed",
        "table_count",
        "equation_count",
        "image_count",
        "preview",
    ]

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build JSON/CSV indexes from converted problem-bank Markdown folders.",
    )
    parser.add_argument("input_root", type=Path)
    parser.add_argument("json_output", type=Path)
    parser.add_argument("--csv-output", type=Path)
    parser.add_argument("--max-preview-chars", type=int, default=220)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = build_problem_bank_index(args.input_root, args.max_preview_chars)
    write_json(records, args.json_output)

    if args.csv_output:
        write_csv(records, args.csv_output)

    print(f"Indexed {len(records)} problem-bank documents.")


if __name__ == "__main__":
    main()
