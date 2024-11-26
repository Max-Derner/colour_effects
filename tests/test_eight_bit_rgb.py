from pytest import mark

from colour_fx.eight_bit import RGB


class TestRGB():
    rgb_vals = [0, 1, 2, 3, 4, 5]

    @mark.parametrize('r', rgb_vals)
    @mark.parametrize('g', rgb_vals)
    @mark.parametrize('b', rgb_vals)
    def test_foreground(self, r, g, b):
        colour = RGB(r, g, b).foreground
        split_val = colour.split(';')

        assert len(split_val) == 3, (
            F"RGB should have 3 values separated by ';', "
            F"found {len(split_val)}"
        )
        assert split_val[0] == '38', (
            "RGB should start with 38 as default to indicate "
            "foreground colour when requesting foreground colour"
        )
        assert split_val[1] == '5', (
            "RGB should use 5 as second component"
        )
        assert 16 <= int(split_val[2]) <= 231, (
            F"RGB colour component should be between 16 and 231 "
            F"inclusive by default to indicate a none brightened colour. "
            F"Got {split_val[2]}"
        )

    @mark.parametrize('r', rgb_vals)
    @mark.parametrize('g', rgb_vals)
    @mark.parametrize('b', rgb_vals)
    def test_background(self, r, g, b):
        colour = RGB(r, g, b).background
        split_val = colour.split(';')

        assert len(split_val) == 3, (
            F"RGB should have 3 values separated by ';', "
            F"found {len(split_val)}"
        )
        assert split_val[0] == '48', (
            "RGB should start with 48 as default to indicate "
            "background colour when requesting background colour"
        )
        assert split_val[1] == '5', (
            "RGB should use 5 as second component"
        )
        assert 16 <= int(split_val[2]) <= 231, (
            F"RGB colour component should be between 16 and 231 "
            F"inclusive. Got {split_val[2]}"
        )
