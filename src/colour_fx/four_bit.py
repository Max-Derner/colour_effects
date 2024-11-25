from enum import Enum
from . import ansi_val


# Taken from section 'Select Graphic Rendition parameters' in
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
    def bright(self) -> ansi_val:
        return str(
            int(self) + 60
        )

    @property
    def background(self) -> ansi_val:
        return str(
            int(self) + 10
        )

    @property
    def bright_background(self) -> ansi_val:
        return str(
            int(self) + 70
        )
