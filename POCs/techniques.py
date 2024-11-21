

def apply_gradient(text: str, colour_codes: list):
    lines_of_text = text.split('\n')
    text_length = max(
        [len(line) for line in lines_of_text]
    )
    colour_codes = colour_codes[:text_length]
    colour_length = text_length // len(colour_codes)
    output = ''
    for line in lines_of_text:
        colour_pos = 0
        for char_pos, char in enumerate(line):
            if char_pos % colour_length == 0:
                output += colour_codes[colour_pos]
                colour_pos += 1
                colour_pos = min(len(colour_codes) - 1, colour_pos)
            output += char
        output += '\n'
    return output


if __name__ == "__main__":
    from bansi_codes import Colour, compile_ansi_code
    from pathlib import Path

    red = compile_ansi_code(foreground=Colour.RED)
    orange = compile_ansi_code(foreground=Colour.RED.bright)
    yellow = compile_ansi_code(foreground=Colour.YELLOW.bright)
    green = compile_ansi_code(foreground=Colour.GREEN)
    blue = compile_ansi_code(foreground=Colour.BLUE)
    indigo = compile_ansi_code(foreground=Colour.BLUE.bright)
    violet = compile_ansi_code(foreground=Colour.MAGENTA)

    codes = [
        red,
        orange,
        yellow,
        green,
        blue,
        indigo,
        violet,
    ]

    sample_path = Path(__file__).parent.joinpath('sample.txt')
    with open(sample_path, mode='r') as f:
        text = f.read()

    print(apply_gradient(text, codes))
