import pkgutil
import importlib
from pathlib import Path
from .command_struct import Command

command_registry = {}
commands_dir = Path(__file__).parent

for _, module_name, _ in pkgutil.iter_modules([str(commands_dir)]):
    module = importlib.import_module(f"commands.{module_name}")
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, type) and issubclass(attr, Command) and attr is not Command:
            cmd_instance = attr()
            command_registry[cmd_instance.name] = cmd_instance
            for alias in getattr(cmd_instance, "aliases", []):
                command_registry[alias] = cmd_instance
