from commandDictionary.command_struct import Command
from emailFunctions import emailjar
from textAnimations.blockReveal import openType
import config

TO = "op.matthew@icloud.com"

class EmailCommand(Command):
    name = "email"
    aliases = ["em"]

    def execute(self, args):
        subject = input("Subject> ").strip()
        if not subject:
            print("Subject cannot be empty.")
            return

        print("Body (type END on a blank line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        body = "\n".join(lines)

        if not body:
            print("Body cannot be empty.")
            return

        success = emailjar.send_email(TO, subject, body)
        openType("Email sent." if success else "Failed to send email.")
        config.clearCheck = False