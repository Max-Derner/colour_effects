from pytest import mark

from colour_fx.effects import apply_ansi_field
from colour_fx.four_bit import Colour


@mark.parametrize('field, text, expected', [
    (
        [
            [[Colour.RED], [], [Colour.BLACK, Colour.CYAN.background]],
            [[], [], []],
            [[Colour.BLACK, Colour.CYAN.background], [], [Colour.RED]],
        ],
        "bananarama\nbananarama\nbananarama",
        (
            "\033[0m\033[31mb\033[0ma\033[0m\033[30;46mn\033[0m\033[31ma"
            "\033[0mn\033[0m\033[30;46ma\033[0m\033[31mr\033[0ma\033[0m"
            "\033[30;46mm\033[0m\033[31ma\033[0m\n\033[0mbananarama\033[0m\n"
            "\033[0m\033[30;46mb\033[0ma\033[0m\033[31mn\033[0m\033[30;46ma"
            "\033[0mn\033[0m\033[31ma\033[0m\033[30;46mr\033[0ma\033[0m"
            "\033[31mm\033[0m\033[30;46ma\033[0m\n"
        )

    )
])
def test_apply_ansi_field(field, text, expected):
    got = apply_ansi_field(text, field)

    double_reset = "\033[0m\033[0m"
    assert expected == got
    assert double_reset not in got
