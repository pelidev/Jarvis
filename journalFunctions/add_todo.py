from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

JOURNAL_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Journals"

def get_today_journal_path(dmod) -> Path:
    now = datetime.now(ZoneInfo("America/Denver")) + timedelta(days=dmod)
    month_folder = JOURNAL_BASE_DIR / now.strftime("%Y-%m")
    month_folder.mkdir(parents=True, exist_ok=True)

    file_name = now.strftime("%Y-%m-%d") + ".txt"
    return month_folder / file_name

def add_todo(dmod: int, task: str):
    journal_path = get_today_journal_path(dmod)
    if not journal_path.exists():
        journal_path.touch()
        now = datetime.now(ZoneInfo("America/Denver")) + timedelta(days=dmod)
        header = (
            "+----------------------+\n"
            f"|  Daily Log {now.strftime('%m/%d/%y')}  |\n"
            "+----------------------+\n\n"
            "ToDo:\n"
            "\n\n"
            "Thoughts:\n\n"
        )
        with open(journal_path, "w") as f:
            f.write(header)

    # read the file (assuming it already has header + sections)
    with open(journal_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    in_todo = False

    for line in lines:
        new_lines.append(line)

        if line.strip() == "ToDo:":
            in_todo = True
            continue

        if in_todo and line.strip().startswith("Thoughts:"):
            new_lines.insert(len(new_lines)-2, f"_ {task}\n")
            in_todo = False

    with open(journal_path, "w") as f:
        f.writelines(new_lines)
