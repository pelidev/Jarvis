from pathlib import Path
from textAnimations.blockReveal import openType
import subprocess

MASTERLOGS_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Masterlogs"


def new_masterlog(name):
    MASTERLOGS_DIR.mkdir(parents=True, exist_ok=True)

    filename = name.strip().lower().replace(" ", "-") + ".txt"
    file_path = MASTERLOGS_DIR / filename

    if file_path.exists():
        openType(f"{filename} already exists. Opening it.")
    else:
        file_path.touch()
        openType(f"Created {filename}")

    subprocess.run(["nvim", str(file_path)])


def open_masterlog():
    MASTERLOGS_DIR.mkdir(parents=True, exist_ok=True)

    logs = sorted([f for f in MASTERLOGS_DIR.glob("*.txt")])

    if not logs:
        openType("No master logs found.")
        openType("Use 'nmlog' to create one.")
        return

    openType("Master Logs:")
    for i, log in enumerate(logs, 1):
        openType(f"  {i}. {log.stem}")

    while True:
        try:
            choice = int(input("\nEnter number: ").strip())
            if 1 <= choice <= len(logs):
                break
            openType("Please enter a valid number.")
        except ValueError:
            openType("Please enter a number.")

    subprocess.run(["nvim", str(logs[choice - 1])])
