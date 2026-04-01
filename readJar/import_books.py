from pathlib import Path
from textAnimations.blockReveal import openType
import json
import shutil

MARKDOWNS_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "markdowns"
BOOKS_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Books"


def import_markdowns():
    MARKDOWNS_DIR.mkdir(parents=True, exist_ok=True)
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted([f for f in MARKDOWNS_DIR.glob("*.md")])

    if not md_files:
        openType("No markdown files found in Jarvis_Data/markdowns.")
        openType("Drop .md files in there and try again.")
        return

    imported = 0
    skipped = 0

    for md_file in md_files:
        folder_name = md_file.stem.lower().replace(" ", "-")
        book_dir = BOOKS_DIR / folder_name

        if book_dir.exists():
            openType(f"Skipping {md_file.name} — already imported.")
            skipped += 1
            continue

        # Create book directory structure
        book_dir.mkdir(parents=True, exist_ok=True)
        (book_dir / "quotes").mkdir(exist_ok=True)

        # Move md file into book dir as book.md
        shutil.move(str(md_file), str(book_dir / "book.md"))

        # Create default state.json
        state = {"last_line": 1}
        with open(book_dir / "state.json", "w") as f:
            json.dump(state, f, indent=2)

        openType(f"Imported: {folder_name}")
        imported += 1

    openType(f"Done. {imported} imported  {skipped} skipped.")
