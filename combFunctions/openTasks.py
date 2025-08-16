from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


JOURNAL_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Journals"

def incompletetasks(days):
    days += 1
    days = range(days)
    tasks = []
    for i in days:
        date_count_set = 0
        now = datetime.now(ZoneInfo("America/Denver")) - timedelta(days=i)
        month_folder = JOURNAL_BASE_DIR / now.strftime("%Y-%m")
        file = month_folder / now.strftime("%Y-%m-%d.txt")

        if not file.exists():
            continue

        with open(file, "r") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("_"):
                if date_count_set == 0:
                    tasks.append(now.strftime("## %a %Y-%m-%d"))
                    date_count_set = 1
                tasks.append(line)
            else:
                pass


    return tasks

########################### Upcoming Task (same thing just backwards) ########################################

def upcomingtasks(days):
    days += 1
    days = range(days)
    tasks = []
    for i in days:
        date_count_set = 0
        now = datetime.now(ZoneInfo("America/Denver")) + timedelta(days=i)
        month_folder = JOURNAL_BASE_DIR / now.strftime("%Y-%m")
        file = month_folder / now.strftime("%Y-%m-%d.txt")

        if not file.exists():
            continue

        with open(file, "r") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("_"):
                if date_count_set == 0:
                    tasks.append(now.strftime("## %a %Y-%m-%d"))
                    date_count_set = 1
                tasks.append(line)
            else:
                pass


    return tasks




