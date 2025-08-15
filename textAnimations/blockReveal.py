import sys
import time
import re

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def visibleLength(s):
    return len(ansi_escape.sub('', s))

def openType(text, delay=.01):
    for char in text:
        if char == ",":
            print()
        else:
            time.sleep(delay)
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
    print()

def blockReaveal(text, classCall, delay=.07):
    # Step 1: print solid block placeholders
    length = visibleLength(text)
    sys.stdout.write("\033[?25l")
    for i in range(length):
        sys.stdout.write(f"{GREEN}█{RESET}")
        sys.stdout.flush()
        time.sleep(delay)  # pause before reveal

    # Step 2: reveal text one character at a time
    sys.stdout.write("\r")  # return to start of line
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.02)

    if classCall == 1:
        print()
        return None
    else:
        sys.stdout.write("\033[?25h")
        return ""
