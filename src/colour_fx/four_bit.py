from enum import Enum
from colour_fx import ansi_val


# Taken from section 'Select Graphic Rendition parameters' in
# https://en.wikipedia.org/wiki/ANSI_escape_code#Control_Sequence_Introducer_commands
# Skipping lots of stuff that's not widely supported
class Style(str, Enum):
    """Produces a 4 bit ANSI style code value which can be inserted
    into an ANSI escape sequence.

    Example:

    ```python
    blinking = Style.BLINK
    ```"""
    BOLD = '1'
    FAINT = '2'
    UNDERLINE = '4'
    BLINK = '5'
    INVERT = '7'
    STRIKE = '9'
    DUNDERLINE = '21'
    # reset codes
    RESET_ALL = '0'
    RESET_FOREGROUND = '39'
    RESET_BACKGROUND = '49'
    RESET_INTENSITY = '22'  # neither bold nor faint
    NO_BLINK = '25'
    NO_INVERT = '27'
    NO_STRIKE = '29'
    NO_UNDERLINE = '24'


class Colour(str, Enum):
    """Produces a 4 bit ANSI colour code value which can be inserted
    into an ANSI escape sequence.

    Produces code for foreground colour by default. Access properties
    `bright`, `background`, and `bright_background` in order to modify
    as appropriate.

    Example:
    ```python
    red_foreground = Colour.RED

    blue_background = Colour.BLUE.background
    """
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
