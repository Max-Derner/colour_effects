from pytest import mark

from colour_fx.eight_bit import SimpleColour


class TestSimpleColor():
    colours = [
        SimpleColour.BLACK,
        SimpleColour.BLUE,
        SimpleColour.CYAN,
        SimpleColour.GREEN,
        SimpleColour.MAGENTA,
        SimpleColour.RED,
        SimpleColour.WHITE,
        SimpleColour.YELLOW,
    ]

    @mark.parametrize('colour', colours)
    def test_form(self, colour: SimpleColour):
        split_val = colour.split(';')

        assert len(split_val) == 3, (
            F"SimpleColours should have 3 values separated by ';', "
            F"found {len(split_val)}"
        )
        assert split_val[0] == '38', (
            "SimpleColours should start with 38 as default to indicate "
            "foreground colour"
        )
        assert split_val[1] == '5', (
            "SimpleColour should use 5 as second component"
        )
        assert 0 <= int(split_val[2]) <= 7, (
            "SimpleColours colour component should be between 0 and 7 "
            "inclusive by default to indicate a none brightened colour"
        )

    @mark.parametrize('colour', colours)
    def test_brighten(self, colour: SimpleColour):
        new_val = colour.bright

        colour_component = int(new_val.split(';')[2])
        background_component = new_val.split(';')[0]

        assert 8 <= colour_component <= 15, (
            "SimpleColours colour component should be between 8 and 15 "
            "inclusive when brightened"
        )
        assert background_component == '38', (
            "SimpleColours background/foreground component should be 38 when "
            "requesting a brightened colour to indicate a foreground colour"
        )

    @mark.parametrize('colour', colours)
    def test_background(self, colour: SimpleColour):
        new_val = colour.background

        colour_component = int(new_val.split(';')[2])
        background_component = new_val.split(';')[0]

        assert background_component == '48', (
            "SimpleColours background/foreground component should be 48 when "
            "requesting a background colour"
        )
        assert 0 <= colour_component <= 7, (
            "SimpleColours colour component should be between 0 and 7 "
            "inclusive when requesting none brightened background colour"
        )

    @mark.parametrize('colour', colours)
    def test_bright_background(self, colour: SimpleColour):
        new_val = colour.bright_background

        colour_component = int(new_val.split(';')[2])
        background_component = new_val.split(';')[0]

        assert background_component == '48', (
            "SimpleColours background/foreground component should be 48 when "
            "requesting a background colour"
        )
        assert 8 <= colour_component <= 15, (
            "SimpleColours colour component should be between 8 and 15 "
            "inclusive when brightened"
        )
