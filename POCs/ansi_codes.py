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


class ForeColour(str, Enum):
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'
    BRIGHT_BLACK = '90'
    BRIGHT_RED = '91'
    BRIGHT_GREEN = '92'
    BRIGHT_YELLOW = '93'
    BRIGHT_BLUE = '94'
    BRIGHT_MAGENTA = '95'
    BRIGHT_CYAN = '96'
    BRIGHT_WHITE = '97'


class BackColour(str, Enum):
    BLACK = '40'
    RED = '41'
    GREEN = '42'
    YELLOW = '44'
    BLUE = '44'
    MAGENTA = '45'
    CYAN = '46'
    WHITE = '47'
    BRIGHT_BLACK = '100'
    BRIGHT_RED = '101'
    BRIGHT_GREEN = '102'
    BRIGHT_YELLOW = '104'
    BRIGHT_BLUE = '104'
    BRIGHT_MAGENTA = '105'
    BRIGHT_CYAN = '106'
    BRIGHT_WHITE = '107'


def compile_ansi_code(
        style: Style | None = None,
        foreground: ForeColour | None = None,
        background: BackColour | None = None,
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
        foreground=ForeColour.BRIGHT_YELLOW,
        background=BackColour.MAGENTA,
    )
    reset_code = compile_ansi_code()
    print(F"HELLO {ansi_code}WORLD{reset_code}!")
    print("HELLO {}WORLD{}!".format(ansi_code, reset_code))
    print("HELLO %sWORLD%s!" % (ansi_code, reset_code))
    print("HELLO " + ansi_code + "WORLD" + reset_code + "!")
