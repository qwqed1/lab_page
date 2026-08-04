"""Extract searchable ALEX2 table rows from the source demo PDF."""

from __future__ import annotations

import json
from pathlib import Path

import pdfplumber
from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "public" / "documents" / "elagin-demo-result.pdf"
OUTPUT = ROOT / "app" / "data" / "demo-report.json"
CLEAN_PDF = ROOT / "public" / "documents" / "elagin-demo-result-clean.pdf"

TOP_LEVEL_SECTIONS = {
    "Пыльца",
    "Клещ",
    "Плесень и дрожжевые грибы",
    "Продукты растительного происхождения",
    "Продукты животного происхождения",
    "Яд перепончатокрылых",
    "Аллергены животных",
    "Другой",
}


def clean(value: str | None) -> str:
    return " ".join((value or "").split())


def main() -> None:
    pages: list[dict] = []
    all_items: list[dict] = []
    category = ""
    section = ""

    with pdfplumber.open(SOURCE) as document:
        for page_number in range(2, 10):
            table = document.pages[page_number - 1].extract_tables()[0]
            page_rows: list[dict] = []

            for raw_row in table[1:]:
                columns = [clean(value) for value in raw_row]
                non_empty = sum(bool(value) for value in columns)

                if non_empty == 1:
                    title = columns[0]
                    level = 1 if title in TOP_LEVEL_SECTIONS else 2
                    if level == 1:
                        category = title
                        section = ""
                    else:
                        section = title
                    page_rows.append({"kind": "section", "level": level, "title": title})
                    continue

                if non_empty < 2:
                    continue

                item = {
                    "kind": "item",
                    "designation": columns[0],
                    "allergen": columns[1],
                    "type": columns[2],
                    "protein": columns[3],
                    "value": columns[4],
                    "category": category,
                    "section": section,
                    "page": page_number,
                }
                page_rows.append(item)
                all_items.append(item)

            pages.append({"number": page_number, "rows": page_rows})

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps({"pages": pages, "items": all_items}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(all_items)} allergen rows to {OUTPUT}")

    reader = PdfReader(SOURCE)
    writer = PdfWriter()
    for source_page in reader.pages:
        source_page.mediabox.lower_left = (0, 42)
        source_page.cropbox.lower_left = (0, 42)
        writer.add_page(source_page)

    with CLEAN_PDF.open("wb") as stream:
        writer.write(stream)
    print(f"Wrote footer-free PDF to {CLEAN_PDF}")


if __name__ == "__main__":
    main()
