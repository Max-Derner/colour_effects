from math import ceil
from bansi_codes import Style, compile_ansi_code


type ansi_sequence = list[list[str]]
type ansi_field = list[ansi_sequence]


def _produce_ansi_field(
        template: str | ansi_field,
        ) -> tuple[int, ansi_field]:
    """accepts either the text for which you wish to create an ANSI
    field, or a previous ANSI field you want copying"""
    if isinstance(template, str):
        split_text = template.split('\n')
        no_lines = len(split_text)
        no_cols = max(
            [len(line) for line in split_text]
        )
        return [
            [[] for _ in range(no_cols)]
            for _ in range(no_lines)
        ]
    elif isinstance(template, ansi_field):
        return [
            col.copy()
            for line in template
            for col in line
        ]
    else:
        raise TypeError("template not 'str' or 'ansi_field'")


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


def create_vertical_gradient(
        template: str | ansi_field,
        ansi_codes: ansi_sequence,
        *,
        step: int = 1,
        indent: int = 0,
        ) -> ansi_field:
    field = _produce_ansi_field(template)
    field_height = len(field)
    field_width = len(field[0])
    ansi_codes = _expand_ansi_codes(field_width, ansi_codes)

    for line_no in range(field_height):
        if line_no != 0 and line_no % step == 0:
            ansi_codes = ansi_codes[indent:] + ansi_codes[:indent]
        for col_no in range(field_width):
            field[line_no][col_no].extend(ansi_codes[col_no])

    return field


def create_horizontal_gradient(
        template: str | ansi_field,
        ansi_codes: ansi_sequence,
        *,
        step: int = 1,
        indent: int = 0,
        ) -> ansi_field:
    field = _produce_ansi_field(template)
    field_height = len(field)
    field_width = len(field[0])
    ansi_codes = _expand_ansi_codes(field_height, ansi_codes)

    array_bias = []
    for col_no in range(field_width):
        step_no = col_no // step
        array_bias.append(step_no * indent)

    for line_no in range(field_height):
        for col_no in range(field_width):
            code_idx = (line_no + array_bias[col_no]) % len(ansi_codes)
            field[line_no][col_no].extend(ansi_codes[code_idx])

    return field


def apply_ansi_field(
        text: str,
        field: ansi_field,
        ) -> str:
    lines_of_text = text.split('\n')
    output = ''
    current_ansi_vals = None
    RESET = compile_ansi_code()
    for line_no, line in enumerate(lines_of_text):
        line_no = line_no % len(field)
        sequence = field[line_no]
        for idx, char in enumerate(line):
            idx = idx % len(sequence)
            if current_ansi_vals != (new_vals := sequence[idx]):
                current_ansi_vals = new_vals
                output += (
                    RESET
                    + compile_ansi_code(*current_ansi_vals)
                    + char
                )
            else:
                output += char
        output += RESET + '\n'
        current_ansi_vals = None
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

    red = [Colour.RED, Style.BOLD]
    orange = [Colour.RED.bright, Style.BOLD]
    yellow = [Colour.YELLOW.bright, Style.BOLD]
    green = [Colour.GREEN, Style.BOLD]
    blue = [Colour.BLUE, Style.BOLD]
    indigo = [Colour.BLUE.bright, Style.BOLD]
    violet = [Colour.MAGENTA, Style.BOLD]

    # red = compile_ansi_code(SimpleColour.RED, SimpleColour.WHITE.background, Style.BOLD)
    # orange = compile_ansi_code(SimpleColour.RED.bright, Style.BOLD)
    # yellow = compile_ansi_code(SimpleColour.YELLOW.bright, Style.BOLD)
    # green = compile_ansi_code(SimpleColour.GREEN, Style.BOLD)
    # blue = compile_ansi_code(SimpleColour.BLUE, Style.BOLD)
    # indigo = compile_ansi_code(SimpleColour.BLUE.bright, Style.BOLD)
    # violet = compile_ansi_code(SimpleColour.MAGENTA, Style.BOLD)

    # red = [RGB(6, 0, 0).foreground, Style.BOLD]
    # orange = [RGB(6, 4, 4).foreground, Style.BOLD]
    # yellow = [RGB(0, 6, 6).foreground, Style.BOLD]
    # green = [RGB(0, 6, 0).foreground, Style.BOLD]
    # blue = [RGB(0, 0, 6).foreground, Style.BOLD]
    # indigo = [RGB(4, 4, 6).foreground, Style.BOLD]
    # violet = [RGB(6, 6, 0).foreground, Style.BOLD]

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
    grey_sequence: ansi_sequence = [
        [Grey.A, Style.BOLD],
        [Grey.B, Style.BOLD],
        [Grey.C, Style.BOLD],
        [Grey.D, Style.BOLD],
        [Grey.E, Style.BOLD],
        [Grey.F, Style.BOLD],
        [Grey.G, Style.BOLD],
        [Grey.H, Style.BOLD],
        [Grey.I, Style.BOLD],
        [Grey.J, Style.BOLD],
        [Grey.K, Style.BOLD],
        [Grey.L, Style.BOLD],
        [Grey.M, Style.BOLD],
        [Grey.N, Style.BOLD],
        [Grey.O, Style.BOLD],
        [Grey.P, Style.BOLD],
        [Grey.Q, Style.BOLD],
        [Grey.R, Style.BOLD],
        [Grey.S, Style.BOLD],
        [Grey.T, Style.BOLD],
        [Grey.U, Style.BOLD],
        [Grey.V, Style.BOLD],
        [Grey.W, Style.BOLD],
        [Grey.X, Style.BOLD],
    ]

    grey_sequence = (
        grey_sequence
        + grey_sequence[-2: 0:-1]
    )

    small_field = [
        [[Colour.RED.bright, Style.BOLD], [Colour.GREEN, Style.BLINK]],
        [[Colour.GREEN, Style.BLINK], [Colour.RED.bright, Style.BOLD]],
    ]

    sample_path = Path(__file__).parent.joinpath('sample_b.txt')
    with open(sample_path, mode='r') as f:
        text = f.read()

    step = 15
    indent = -1

    # output = apply_shimmer(text, 3)
    # gradient_field = create_vertical_gradient(
    #     text,
    #     grey_sequence,
    #     step=1,
    #     indent=0
    # )
    gradient_field = create_horizontal_gradient(
        text,
        colour_codes,
        step=1,
        indent=0
    )
    output = apply_ansi_field(text, small_field)

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
