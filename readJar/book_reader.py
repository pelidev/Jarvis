from pathlib import Path
from textAnimations.blockReveal import openType
import subprocess
import json

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
    return {"last_line": 1}


def _open_book(book_dir, line_number=1):
    book_file = book_dir / "book.md"
    state_path = str(book_dir / "state.json")
    book_folder_name = book_dir.name

    # Save last read globally
    _save_last_read(book_folder_name)

    # Neovim autocommand: on VimLeave write current line to this book's state.json
    nvim_cmd = (
        f'autocmd VimLeave * call writefile(['
        f'"{{\\\"last_line\\\": " . line(".") . "}}"'
        f'], "{state_path}")'
    )

    subprocess.run([
        "nvim",
        f"+{line_number}",
        f"+{nvim_cmd}",
        str(book_file)
    ])


def list_and_open_book():
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)

    books = sorted([d for d in BOOKS_DIR.iterdir() if d.is_dir() and (d / "book.md").exists()])

    if not books:
        openType("No books found in your library.")
        openType("Drop .md files into Jarvis_Data/markdowns and run importmds.")
        return

    openType("Your library:")
    for i, book in enumerate(books, 1):
        state = _load_book_state(book)
        line = state.get("last_line", 1)
        openType(f"  {i}. {book.name}  [line {line}]")

    while True:
        try:
            choice = int(input("\nEnter number: ").strip())
            if 1 <= choice <= len(books):
                break
            openType("Please enter a valid number.")
        except ValueError:
            openType("Please enter a number.")

    book_dir = books[choice - 1]
    state = _load_book_state(book_dir)
    line_number = state.get("last_line", 1)

    openType(f"Opening {book_dir.name} at line {line_number}")
    _open_book(book_dir, line_number)


def resume_last_book():
    last = _load_last_read()

    if not last or "last_book" not in last:
        openType("No book on record. Use 'read' to open one first.")
        return

    book_dir = BOOKS_DIR / last["last_book"]

    if not book_dir.exists() or not (book_dir / "book.md").exists():
        openType(f"Could not find {last['last_book']} in your library.")
        openType("It may have been moved or renamed.")
        return

    state = _load_book_state(book_dir)
    line_number = state.get("last_line", 1)

    openType(f"Resuming {book_dir.name} at line {line_number}")
    _open_book(book_dir, line_number)
