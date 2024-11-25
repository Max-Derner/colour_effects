from colour_fx.four_bit import Colour, Style
from pytest import mark


@mark.parametrize('got, want',
                  [
                      (Colour.BLACK, '30'),
                      (Colour.RED.bright, '91'),
                      (Colour.MAGENTA.background, '45'),
                      (Colour.CYAN.bright_background, '106'),
                  ])
def test_colour(got, want):
    assert got == want


def test_style():
    assert Style.DUNDERLINE == '21'
