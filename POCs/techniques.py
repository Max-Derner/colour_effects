from math import ceil
from bansi_codes import Style, compile_ansi_code


# This whole thing needs a rejig
#
# These apply functions should simply add ansi vals into a 3D array of
# array[lines][columns][vals]
# Apply ansi codes should then compile the vals into codes


def apply_shimmer(text: str, spread: int) -> str:
    BLINK_CODE = compile_ansi_code(Style.BLINK)
    RESET_CODE = compile_ansi_code()
    output = ''
    for line_no, line in enumerate(text.split('\n')):
        # print('a')
        for col_no, char in enumerate(line):
            # print('b')
            if (line_no + col_no) % spread == 0:
                output += BLINK_CODE + char + RESET_CODE
            else:
                output += char
        output += '\n'
    return output


def apply_vertical_gradient(
        text: str,
        ansi_codes: list,
        *,
        step: int = 1,
        indent: int = 1,
        ) -> str:
    lines_of_text = text.split('\n')
    text_length = max(
        [len(line) for line in lines_of_text]
    )
    ansi_codes = _expand_ansi_codes(text_length, ansi_codes)

    code_array = []
    for line_no in range(len(lines_of_text)):
        if line_no != 0 and line_no % step == 0:
            ansi_codes = ansi_codes[indent:] + ansi_codes[:indent]
        code_array.append(ansi_codes)

    return apply_ansi_codes(lines_of_text, code_array)


def apply_horizontal_gradient(
        text: str,
        ansi_codes: list,
        *,
        step: int = 1,
        indent: int = 1,
        ) -> str:
    lines_of_text = text.split('\n')
    text_depth = len(lines_of_text)
    text_length = max(
        [len(line) for line in lines_of_text]
    )
    ansi_codes = _expand_ansi_codes(text_depth, ansi_codes)

    array_bias = []
    for col_no in range(text_length):
        step_no = col_no // step
        array_bias.append(step_no * indent)

    code_array = []
    for line_no in range(text_depth):
        code_line = []
        for col_no in range(text_length):
            code_idx = (line_no + array_bias[col_no]) % len(ansi_codes)
            code_line.append(ansi_codes[code_idx])
        code_array.append(code_line)

    return apply_ansi_codes(lines_of_text, code_array)


def apply_ansi_codes(
        lines_of_text: list[str],
        ansi_array: list[list[str]]
        ) -> str:
    output = ''
    current_code = None
    RESET = compile_ansi_code()
    for line_no, line in enumerate(lines_of_text):
        codes = ansi_array[line_no]
        for idx, char in enumerate(line):
            idx = idx % len(codes)
            if current_code != (new_code := codes[idx]):
                current_code = new_code
                output += current_code + char
            else:
                output += char
        output += RESET + '\n'
        current_code = None
    return output


def _expand_ansi_codes(
        array_length: int,
        ansi_codes: list[str],
        ) -> list[str]:
    """expands a list of ANSI codes to a new length such that any code
    appearing before another code in the original list will not appear
    after that code in the new list.

    Example:

    [1, 2, 3] with new length 6 gives [1, 1, 2, 2, 3, 3]"""
    colour_length = ceil(array_length / len(ansi_codes))
    return [
        ansi_code
        for ansi_code in ansi_codes
        for _ in range(colour_length)
    ]


if __name__ == "__main__":
    from bansi_codes import Colour
    from eight_bit_codes import SimpleColour, RGB, Grey
    from pathlib import Path

    # red = compile_ansi_code(Colour.RED, Style.BOLD)
    # orange = compile_ansi_code(Colour.RED.bright, Style.BOLD)
    # yellow = compile_ansi_code(Colour.YELLOW.bright, Style.BOLD)
    # green = compile_ansi_code(Colour.GREEN, Style.BOLD)
    # blue = compile_ansi_code(Colour.BLUE, Style.BOLD)
    # indigo = compile_ansi_code(Colour.BLUE.bright, Style.BOLD)
    # violet = compile_ansi_code(Colour.MAGENTA, Style.BOLD)

    # red = compile_ansi_code(SimpleColour.RED, SimpleColour.WHITE.background, Style.BOLD)
    # orange = compile_ansi_code(SimpleColour.RED.bright, Style.BOLD)
    # yellow = compile_ansi_code(SimpleColour.YELLOW.bright, Style.BOLD)
    # green = compile_ansi_code(SimpleColour.GREEN, Style.BOLD)
    # blue = compile_ansi_code(SimpleColour.BLUE, Style.BOLD)
    # indigo = compile_ansi_code(SimpleColour.BLUE.bright, Style.BOLD)
    # violet = compile_ansi_code(SimpleColour.MAGENTA, Style.BOLD)

    red = compile_ansi_code(RGB(6, 0, 0).foreground, Style.BOLD)
    orange = compile_ansi_code(RGB(6, 4, 4).foreground, Style.BOLD)
    yellow = compile_ansi_code(RGB(0, 6, 6).foreground, Style.BOLD)
    green = compile_ansi_code(RGB(0, 6, 0).foreground, Style.BOLD)
    blue = compile_ansi_code(RGB(0, 0, 6).foreground, Style.BOLD)
    indigo = compile_ansi_code(RGB(4, 4, 6).foreground, Style.BOLD)
    violet = compile_ansi_code(RGB(6, 6, 0).foreground, Style.BOLD)

    # red = compile_ansi_code(Colour.RED.background)
    # orange = compile_ansi_code(Colour.RED.bright_background)
    # yellow = compile_ansi_code(Colour.YELLOW.bright_background)
    # green = compile_ansi_code(Colour.GREEN.background)
    # blue = compile_ansi_code(Colour.BLUE.background)
    # indigo = compile_ansi_code(Colour.BLUE.bright_background)
    # violet = compile_ansi_code(Colour.MAGENTA.background)

    # red = compile_ansi_code(Colour.RED.background, Style.BLINK)
    # orange = compile_ansi_code(Colour.RED.bright_background, Style.BLINK)
    # yellow = compile_ansi_code(Colour.YELLOW.bright_background, Style.BLINK)
    # green = compile_ansi_code(Colour.GREEN.background, Style.BLINK)
    # blue = compile_ansi_code(Colour.BLUE.background, Style.BLINK)
    # indigo = compile_ansi_code(Colour.BLUE.bright_background, Style.BLINK)
    # violet = compile_ansi_code(Colour.MAGENTA.background, Style.BLINK)

    colour_codes = [
        red,
        orange,
        yellow,
        green,
        blue,
        indigo,
        violet,
    ]
    grey_codes = [
        compile_ansi_code(Grey.A.foreground, Style.BOLD),
        compile_ansi_code(Grey.B.foreground, Style.BOLD),
        compile_ansi_code(Grey.C.foreground, Style.BOLD),
        compile_ansi_code(Grey.D.foreground, Style.BOLD),
        compile_ansi_code(Grey.E.foreground, Style.BOLD),
        compile_ansi_code(Grey.F.foreground, Style.BOLD),
        compile_ansi_code(Grey.G.foreground, Style.BOLD),
        compile_ansi_code(Grey.H.foreground, Style.BOLD),
        compile_ansi_code(Grey.I.foreground, Style.BOLD),
        compile_ansi_code(Grey.J.foreground, Style.BOLD),
        compile_ansi_code(Grey.K.foreground, Style.BOLD),
        compile_ansi_code(Grey.L.foreground, Style.BOLD),
        compile_ansi_code(Grey.M.foreground, Style.BOLD),
        compile_ansi_code(Grey.N.foreground, Style.BOLD),
        compile_ansi_code(Grey.O.foreground, Style.BOLD),
        compile_ansi_code(Grey.P.foreground, Style.BOLD),
        compile_ansi_code(Grey.Q.foreground, Style.BOLD),
        compile_ansi_code(Grey.R.foreground, Style.BOLD),
        compile_ansi_code(Grey.S.foreground, Style.BOLD),
        compile_ansi_code(Grey.T.foreground, Style.BOLD),
        compile_ansi_code(Grey.U.foreground, Style.BOLD),
        compile_ansi_code(Grey.V.foreground, Style.BOLD),
        compile_ansi_code(Grey.W.foreground, Style.BOLD),
        compile_ansi_code(Grey.X.foreground, Style.BOLD),
    ]

    sample_path = Path(__file__).parent.joinpath('sample_b.txt')
    with open(sample_path, mode='r') as f:
        text = f.read()

    step = 15
    indent = -1

    # output = apply_shimmer(text, 3)
    output = apply_vertical_gradient(text, grey_codes, step=1, indent=2)

    from pathlib import Path
    output_path = Path(
        __file__
        ).parent.parent.joinpath(
            'zzz'
            ).joinpath(
                'output.txt'
                )
    with open(output_path, mode='w') as f:
        f.write(output)
    print(output)
