from enum import Enum
from typing import Literal

from colour_fx._util import ansi_val


def _eight_bit_brighten(eight_bit_ansi_val: ansi_val) -> ansi_val:
    split_code = eight_bit_ansi_val.split(';')
    colour_section = split_code[-1]
    colour_section = str(
        int(colour_section) + 8
    )
    split_code[-1] = colour_section
    return ';'.join(split_code)


def _eight_bit_background_mod(eight_bit_ansi_val: ansi_val) -> ansi_val:
    split_code = eight_bit_ansi_val.split(';')
    split_code[0] = '48'
    return ';'.join(split_code)


class SimpleColour(str, Enum):
    """Produces an 8 bit colour code which can be inserted into an ANSI
    escape sequence.

    Produces code for foreground colour by default. Access properties
    `bright`, `background`, and `bright_background` in order to modify
    as appropriate.

    Example:
    ```python
    red_foreground = SimpleColour.RED

    blue_background = SimpleColour.BLUE.background
    ```"""
    BLACK = '38;5;0'
    RED = '38;5;1'
    GREEN = '38;5;2'
    YELLOW = '38;5;3'
    BLUE = '38;5;4'
    MAGENTA = '38;5;5'
    CYAN = '38;5;6'
    WHITE = '38;5;7'

    @property
    def bright(self) -> ansi_val:
        return _eight_bit_brighten(self)

    @property
    def background(self) -> ansi_val:
        return _eight_bit_background_mod(self)

    @property
    def bright_background(self) -> ansi_val:
        return _eight_bit_background_mod(
            _eight_bit_brighten(self)
        )


class Grey(str, Enum):
    """Produces an 8 bit ANSI colour code value which can be inserted
    into an ANSI escape sequence. There are 24 greys represented by 2
    letter combinations. The first letter maps as follows:

    * A -> black
    * B -> dark grey
    * C -> light grey
    * D -> white

    The second letter is then a choice of A (darkest) to F (lightest)

    Produces code for foreground colour by default. Access property
    `background` for background colour code.

    Example:
    ```python
    dark_grey = CSI + Grey.BC + SGR
    ```"""
    AA = '38;5;232'
    AB = '38;5;233'
    AC = '38;5;234'
    AD = '38;5;235'
    AE = '38;5;236'
    AF = '38;5;237'
    BA = '38;5;238'
    BB = '38;5;239'
    BC = '38;5;240'
    BD = '38;5;241'
    BE = '38;5;242'
    BF = '38;5;243'
    CA = '38;5;244'
    CB = '38;5;245'
    CC = '38;5;246'
    CD = '38;5;247'
    CE = '38;5;248'
    CF = '38;5;249'
    DA = '38;5;250'
    DB = '38;5;251'
    DC = '38;5;252'
    DD = '38;5;253'
    DE = '38;5;254'
    DF = '38;5;255'

    @property
    def background(self) -> ansi_val:
        return _eight_bit_background_mod(self)


class RGB:
    """Accepts rgb values between 0 and 5 inclusive, then produces ANSI
    values when requested via the foreground and background properties"""
    def __init__(self,
                 r: Literal[0, 1, 2, 3, 4, 5],
                 g: Literal[0, 1, 2, 3, 4, 5],
                 b: Literal[0, 1, 2, 3, 4, 5],
                 ):
        # maths taken from:
        # https://en.wikipedia.org/wiki/ANSI_escape_code#Control_Sequence_Introducer_commands
        # 16-231:  6 × 6 × 6 cube (216 colors):
        #       16 + 36 × r + 6 × g + b (0 ≤ r, g, b ≤ 5)
        self._colour_component = str(
            16
            + 36 * r
            + 6 * g
            + b
        )

    @property
    def foreground(self) -> ansi_val:
        return '38;5;' + self._colour_component

    @property
    def background(self) -> ansi_val:
        return '48;5;' + self._colour_component
