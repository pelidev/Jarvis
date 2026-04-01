from pathlib import Path
from textAnimations.blockReveal import openType
import json
import os

BOOKS_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Books"
LAST_READ_FILE = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "last_read.json"


def _load_last_read():
    if LAST_READ_FILE.exists():
        with open(LAST_READ_FILE, "r") as f:
            return json.load(f)
    return {}


def _save_last_read(book_folder_name):
    data = {"last_book": book_folder_name}
    with open(LAST_READ_FILE, "w") as f:
        json.dump(data, f, indent=2)


def _load_book_state(book_dir):
    state_file = book_dir / "state.json"
    if state_file.exists():
        with open(state_file, "r") as f:
            return json.load(f)
    return {"last_line": 0}


def _save_book_state(book_dir, paragraph_index):
    state_file = book_dir / "state.json"
    state = _load_book_state(book_dir)
    state["last_line"] = paragraph_index
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)


def _run_reader(book_dir, lines_per_page):
    book_file = book_dir / "book.md"
    state = _load_book_state(book_dir)
    current = max(0, state.get("last_line", 0))

    with open(book_file, "r", encoding="utf-8") as f:
        paragraphs = [line.rstrip() for line in f.readlines()]

    total = len(paragraphs) / 2

    if current >= total:
        openType("You've reached the end of the book.")
        return

    _save_last_read(book_dir.name)
    para = state.get("last_line", 0)
    with open(book_file, "r", encoding="utf-8") as f:
        book_total = sum(1 for line in f)  # count everything
    percent = int((para / book_total) * 100) if book_total > 0 else 0
    openType(f"Resuming {book_dir.name} — {percent}% complete")
    print()

    while current < total:
        os.system('clear')

        chunk_start = current
        chunk = []
        temp = current
        count = 0
        while temp < total and count < lines_per_page:
            chunk.append(paragraphs[temp])
            if paragraphs[temp]:
                count += 1
            temp += 1

        current = temp

        for para in chunk:
            if para:
                print(para)
                print()

        _save_book_state(book_dir, chunk_start)

        if current >= total:
            print("--- End of book ---")
            break

        try:
            user_input = input("Enter or Q").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            openType("Position saved. Come back with 'ares' to continue.")
            break

        if user_input == "q":
            openType("Position saved. Come back with 'ares' to continue.")
            break


def active_read(lines_per_page=5):
    last = _load_last_read()

    if not last or "last_book" not in last:
        openType("No book on record. Use 'aread' to select one first.")
        return

    book_dir = BOOKS_DIR / last["last_book"]

    if not book_dir.exists() or not (book_dir / "book.md").exists():
        openType(f"Could not find {last['last_book']} in your library.")
        return

    _run_reader(book_dir, lines_per_page)


def active_read_select(lines_per_page=5):
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)

    books = sorted([d for d in BOOKS_DIR.iterdir() if d.is_dir() and (d / "book.md").exists()])

    if not books:
        openType("No books found in your library.")
        openType("Drop .md files into Jarvis_Data/markdowns and run importmds.")
        return

    openType("Your library:")
    for i, book in enumerate(books, 1):
        state = _load_book_state(book)
        para = state.get("last_line", 0)
        with open(book / "book.md", "r", encoding="utf-8") as f:
            book_total = sum(1 for line in f)  # count everything
        percent = int((para / book_total) * 100) if book_total > 0 else 0
        openType(f"  {i}. {book.name}  [{percent}% complete]")

    while True:
        try:
            choice = int(input("\nEnter number: ").strip())
            if 1 <= choice <= len(books):
                break
            openType("Please enter a valid number.")
        except ValueError:
            openType("Please enter a number.")

    book_dir = books[choice - 1]
    _save_last_read(book_dir.name)
    _run_reader(book_dir, lines_per_page)
