from typing import TypeAlias

ansi_val: TypeAlias = str
ansi_code: TypeAlias = str
ansi_val_collection: TypeAlias = list[list[ansi_val]]
ansi_field: TypeAlias = list[ansi_val_collection]

# Control Sequence Introducer
CSI = '\033['

# Select Graphic Rendition
SGR = 'm'


def compile_ansi_code(*ansi_vals: ansi_val) -> ansi_code:
    """Feed in any number of colour and style ANSI values and get a
    compiled ANSI code.

    Example:

    ```python
    compile_ansi_code(
        Colour.RED.bright,
        Colour.BLACK.bright_background,
        Style.BLINK,
        Style.BOLD
    )
    ```"""
    ansi_vals = ansi_vals or ('0', )
    return CSI + ';'.join(ansi_vals) + SGR
