from math import ceil
from bansi_codes import Style, compile_ansi_code


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
    colour_array = _build_colour_array(text_length, ansi_codes)
    output = ''
    current_code = None
    RESET = compile_ansi_code()
    for line_no, line in enumerate(lines_of_text):
        if line_no != 0 and line_no % step == 0:
            colour_array = colour_array[indent:] + colour_array[:indent]
        for idx, char in enumerate(line):
            idx = idx % len(colour_array)
            if current_code != (new_code := colour_array[idx]):
                current_code = new_code
                output += current_code + char
            else:
                output += char
        output += RESET + '\n'
        current_code = None
    return output


def _build_colour_array(
        array_length: int,
        ansi_codes: list[str],
        ) -> list[str]:
    """expands a list of ANSI codes to a new length such that any code
    appearing before another code in the original list will not appear 
    after that code in the new list.

    Example:

    [1, 2, 3] with new length 6 gives [1, 1, 2, 2, 3, 3]"""
    colour_length = ceil(array_length / len(ansi_codes))
    colour_array = [
        ansi_code
        for ansi_code in ansi_codes
        for _ in range(colour_length)
    ]
    return colour_array


if __name__ == "__main__":
    from bansi_codes import Colour
    from pathlib import Path

    red = compile_ansi_code(Colour.RED, Style.BOLD)
    orange = compile_ansi_code(Colour.RED.bright, Style.BOLD)
    yellow = compile_ansi_code(Colour.YELLOW.bright, Style.BOLD)
    green = compile_ansi_code(Colour.GREEN, Style.BOLD)
    blue = compile_ansi_code(Colour.BLUE, Style.BOLD)
    indigo = compile_ansi_code(Colour.BLUE.bright, Style.BOLD)
    violet = compile_ansi_code(Colour.MAGENTA, Style.BOLD)

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

    codes = [
        red,
        orange,
        yellow,
        green,
        blue,
        indigo,
        violet,
    ]

    sample_path = Path(__file__).parent.joinpath('promo_sample.txt')
    with open(sample_path, mode='r') as f:
        text = f.read()

    output = apply_vertical_gradient(text, codes, step=1, indent=11)
    from pathlib import Path
    output_path = Path(__file__).parent.parent.joinpath('zzz').joinpath('output.txt')
    with open(output_path, mode='w') as f:
        f.write(output)
    print(output)
