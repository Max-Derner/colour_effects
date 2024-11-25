from enum import Enum


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
    def bright(self):
        split_code = self.split(';')
        colour_section = split_code[-1]
        colour_section = str(
            int(colour_section) + 8
        )
        split_code[-1] = colour_section
        return ';'.join(split_code)

    @property
    def background(self):
        split_code = self.split(';')
        split_code[0] = '48'
        return ';'.join(split_code)

    @property
    def bright_background(self):
        split_code = self.split(';')
        colour_section = split_code[-1]
        colour_section = str(
            int(colour_section) + 8
        )
        split_code[-1] = colour_section
        split_code[0] = '48'
        return ';'.join(split_code)


class Grey(str, Enum):
    """Produces an 8 bit colour code which can be inserted into an ANSI
    escape sequence. `A` produces a black, `X` produces a white and the
    letters in between produce varying degrees of grey.

    Produces code for foreground colour by default. Access property
    `background` for background colour code.

    Example:
    ```python
    dark_grey = '\033[' + Grey.F + 'm'
    ```"""
    A = '38;5;232'
    B = '38;5;233'
    C = '38;5;234'
    D = '38;5;235'
    E = '38;5;236'
    F = '38;5;237'
    G = '38;5;238'
    H = '38;5;239'
    I = '38;5;240'
    J = '38;5;241'
    K = '38;5;242'
    L = '38;5;243'
    M = '38;5;244'
    N = '38;5;245'
    O = '38;5;246'
    P = '38;5;247'
    Q = '38;5;248'
    R = '38;5;249'
    S = '38;5;250'
    T = '38;5;251'
    U = '38;5;252'
    V = '38;5;253'
    W = '38;5;254'
    X = '38;5;255'

    @property
    def background(self):
        split_code = self.split(';')
        split_code[0] = '48'
        return ';'.join(split_code)


class RGB:
    def __init__(self, r, g, b):
        self._val = str(
            16
            + 36 * r
            + 6 * g
            + b
        )

    @property
    def foreground(self) -> str:
        return '38;5;' + self._val

    @property
    def background(self) -> str:
        return '48;5;' + self._val
