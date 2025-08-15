class Command:

    name = ""       # command name string
    aliases = []    # optional aliases

    def execute(self, args):
        """Run the command with given arguments"""
        raise NotImplementedError("Commands must implement execute()")
