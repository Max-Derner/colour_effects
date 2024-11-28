from colour_fx._util import compile_ansi_code, CSI, SGR


def test_compile_ansi_code():
    vals = ['0', '1', '2']

    code = compile_ansi_code(*vals)

    assert code == F"{CSI}0;1;2{SGR}"


def test_compile_ansi_code_defaults_to_reset_code():

    code = compile_ansi_code()

    assert code == F"{CSI}0{SGR}"
