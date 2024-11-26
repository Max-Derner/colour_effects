from colour_fx.four_bit import Colour, Style
from pytest import mark


class TestColour:

    colours = [
        Colour.BLACK,
        Colour.BLUE,
        Colour.CYAN,
        Colour.GREEN,
        Colour.MAGENTA,
        Colour.RED,
        Colour.WHITE,
        Colour.YELLOW,
    ]

    @mark.parametrize('colour', colours)
    def test_default_form(self, colour: Colour):
        assert len(colour) <= 3, (
            "default ANSI val for 4 bit Colours should be length 2"
        )
        colour_component = int(colour[-1:])
        assert 0 <= colour_component <= 7, (
            "colour component out of range for 4 bit ANSI vals"
        )
        foreground_component = int(colour[:-1])
        assert foreground_component == 3, (
            "foreground/background component should default to 3 to indicate "
            "a foreground colour"
        )

    @mark.parametrize('colour', colours)
    def test_brighten(self, colour: Colour):
        value = colour.bright

        assert len(value) == 2, (
            "ANSI val for 4 bit bright Colours should be length 2"
        )
        colour_component = int(value[-1:])
        assert 0 <= colour_component <= 7, (
            "colour component out of range for 4 bit ANSI vals"
        )
        foreground_component = int(value[:-1])
        assert foreground_component == 9, (
            "foreground/background component should be 9 to indicate a "
            "bright foreground colour"
        )

    @mark.parametrize('colour', colours)
    def test_background(self, colour: Colour):
        value = colour.background

        assert len(value) == 2, (
            "ANSI val for 4 bit background Colours should be length 2"
        )
        colour_component = int(value[-1:])
        assert 0 <= colour_component <= 7, (
            "colour component out of range for 4 bit ANSI vals"
        )
        foreground_component = int(value[:-1])
        assert foreground_component == 4, (
            "foreground/background component should be 9 to indicate a "
            "background colour"
        )

    @mark.parametrize('colour', colours)
    def test_bright_background(self, colour: Colour):
        value = colour.bright_background

        assert len(value) == 3, (
            "ANSI val for 4 bit bright background Colours should be length 3"
        )
        colour_component = int(value[-1:])
        assert 0 <= colour_component <= 7, (
            "colour component out of range for 4 bit ANSI vals"
        )
        foreground_component = int(value[:-1])
        assert foreground_component == 10, (
            "foreground/background component should be 10 to indicate a "
            "background colour"
        )


@mark.parametrize('got, want', [
    (Style.BOLD, '1'),
    (Style.FAINT, '2'),
    (Style.UNDERLINE, '4'),
    (Style.BLINK, '5'),
    (Style.STRIKE, '9'),
    (Style.DUNDERLINE, '21'),
    (Style.RESET_ALL, '0'),
    (Style.RESET_FOREGROUND, '39'),
    (Style.RESET_BACKGROUND, '49'),
    (Style.RESET_INTENSITY, '22'),
    (Style.NO_BLINK, '25'),
    (Style.NO_STRIKE, '29'),
    (Style.NO_UNDERLINE, '24'),
])
def test_styles(got: Style, want: str):
    assert got == want, "Style incorrectly mapped"


def test_num_styles():
    assert len(Style) == 13, (
        "Number of styles changed, must modify "
        "'test_styles' test to capture change"
    )
