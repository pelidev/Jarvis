from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.document import Document


def single_line_selector(message: str, options: list[str]) -> str:
    if not options:
        raise ValueError("No options to select from.")

    session = PromptSession()
    kb = KeyBindings()
    idx = 0  # start at first option

    def _set_text(event, text: str):
        buf = event.app.current_buffer
        buf.set_document(Document(text=text, cursor_position=len(text)))

    @kb.add("up")
    def _(event):
        nonlocal idx
        idx = (idx - 1) % len(options)
        _set_text(event, options[idx])

    @kb.add("down")
    def _(event):
        nonlocal idx
        idx = (idx + 1) % len(options)
        _set_text(event, options[idx])

    # prefill input with first option; arrows will swap it
    return session.prompt(f"{message} ", default=options[idx], key_bindings=kb, complete_while_typing=False)
