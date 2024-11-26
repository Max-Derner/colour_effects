from pytest import mark

from colour_fx.eight_bit import Grey


class TestGrey():
    greys = [
        Grey.AA, Grey.BA, Grey.CA, Grey.DA,
        Grey.AB, Grey.BB, Grey.CB, Grey.DB,
        Grey.AC, Grey.BC, Grey.CC, Grey.DC,
        Grey.AD, Grey.BD, Grey.CD, Grey.DD,
        Grey.AE, Grey.BE, Grey.CE, Grey.DE,
        Grey.AF, Grey.BF, Grey.CF, Grey.DF,
    ]

    @mark.parametrize('colour', greys)
    def test_form(self, colour: Grey):
        split_val = colour.split(';')

        assert len(split_val) == 3, (
            F"Greys should have 3 values separated by ';', "
            F"found {len(split_val)}"
        )
        assert split_val[0] == '38', (
            "Greys should start with 38 as default to indicate "
            "foreground colour"
        )
        assert split_val[1] == '5', (
            "Greys should use 5 as second component"
        )
        assert 232 <= int(split_val[2]) <= 255, (
            F"Greys colour component should be between 232 and 255 "
            F"inclusive. Got {split_val[2]}"
        )

    @mark.parametrize('colour', greys)
    def test_background(self, colour: Grey):
        new_val = colour.background

        background_component = new_val.split(';')[0]

        assert background_component == '48', (
            "Greys background/foreground component should be 48 when "
            "requesting a background colour"
        )
