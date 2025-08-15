from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import subprocess

JOURNAL_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Journals"

def get_today_journal_path(dmod) -> Path:
    now = datetime.now(ZoneInfo("America/Denver")) + timedelta(days=dmod)
    month_folder = JOURNAL_BASE_DIR / now.strftime("%Y-%m")
    month_folder.mkdir(parents=True, exist_ok=True)

    file_name = now.strftime("%Y-%m-%d") + ".txt"
    return month_folder / file_name

def open_today_journal(launch, dmod):
    journal_path = get_today_journal_path(dmod)
    if not journal_path.exists():
        journal_path.touch()
    if launch == 0:
        subprocess.run(["micro", str(journal_path)])
    else:
        subprocess.run(["nano", str(journal_path)])
