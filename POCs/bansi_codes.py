from enum import Enum


# Control Sequence Introducer
CSI = '\033['


# Taken from section  'Select Graphic Rendition parameters' in
# https://en.wikipedia.org/wiki/ANSI_escape_code#Control_Sequence_Introducer_commands
# Skipping lots of stuff that's not widely supported
class Style(str, Enum):
    RESET = '0'
    BOLD = '1'
    FAINT = '2'
    UNDERLINE = '4'
    BLINK = '5'
    STRIKE = '9'
    DUNDERLINE = '21'


class Colour(str, Enum):
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'

    @property
    def bright(self):
        return str(
            int(self) + 60
        )

    @property
    def background(self):
        return str(
            int(self) + 10
        )

    @property
    def bright_background(self):
        return str(
            int(self) + 70
        )


def compile_ansi_code(*ansi_vals) -> str:
    """Feed in any number of colours and styles and get a compiled ANSI
    code.

    Example:

    ```python
    compile_ansi_code(
        Colour.RED.bright,
        Colour.BLACK.bright_background,
        Style.BLINK,
        Style.BOLD
    )
    ```"""
    ansi_vals = ansi_vals or (Style.RESET, )
    return CSI + ';'.join(ansi_vals) + 'm'


if __name__ == "__main__":
    ansi_code = compile_ansi_code(
        Style.BLINK,
        Colour.YELLOW.bright,
        Colour.MAGENTA.background,
    )
    reset_code = compile_ansi_code()
    print(F"HELLO {ansi_code}WORLD{reset_code}!")
    print("HELLO {}WORLD{}!".format(ansi_code, reset_code))
    print("HELLO %sWORLD%s!" % (ansi_code, reset_code))
    print("HELLO " + ansi_code + "WORLD" + reset_code + "!")
