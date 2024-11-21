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


def compile_ansi_code(
        style: Style | None = None,
        foreground: str | None = None,
        background: str | None = None,
        ) -> str:
    code = CSI
    style = style or Style.RESET
    code += style + ';'
    if foreground is not None:
        code += foreground + ';'
    if background is not None:
        code += background
    return code.strip(';') + 'm'


if __name__ == "__main__":
    ansi_code = compile_ansi_code(
        style=Style.BLINK,
        foreground=Colour.YELLOW.bright,
        background=Colour.MAGENTA.background,
    )
    reset_code = compile_ansi_code()
    print(F"HELLO {ansi_code}WORLD{reset_code}!")
    print("HELLO {}WORLD{}!".format(ansi_code, reset_code))
    print("HELLO %sWORLD%s!" % (ansi_code, reset_code))
    print("HELLO " + ansi_code + "WORLD" + reset_code + "!")
