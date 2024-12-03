from pytest import mark, raises

from colour_fx.effects import (
    produce_ansi_field,
    _is_valid_template,
)


@mark.parametrize('feed_in, expected_out', [
    (
        ' \n\n          \n\n ',
        [
            [[] for _ in range(10)]
            for _ in range(5)
        ]
    ),
    (

        [
            [[] for _ in range(10)]
            for _ in range(5)
        ],

        [
            [[] for _ in range(10)]
            for _ in range(5)
        ]
    ),
    (
        [
            [['a', 'p', 'e'], ['b', 'e', 'd'], ['c', 'a', 't']],
            [['h'], ['i'], []],
            [['h', 'a', 'p', 'p', 'y'], [], ['p', 'a', 't', 'h']]
        ],
        [
            [['a', 'p', 'e'], ['b', 'e', 'd'], ['c', 'a', 't']],
            [['h'], ['i'], []],
            [['h', 'a', 'p', 'p', 'y'], [], ['p', 'a', 't', 'h']]
        ]
    )

])
def test_produce_ansi_field_happy_path(feed_in, expected_out):
    from pprint import pprint
    pprint(feed_in)

    got = produce_ansi_field(feed_in)

    assert expected_out == got
    assert feed_in is not got, (
        "first dimensional copy failed"
    )
    if not isinstance(feed_in, str):
        for line_no, line_in in enumerate(feed_in):
            assert line_in is not got[line_no], (
                "second dimensional copy failed"
            )
            for col_no, col_in in enumerate(line_in):
                assert col_in is not got[line_no][col_no], (
                    "third dimensional copy failed"
                )


poor_templates = [
    # incorrect types
    1,
    1.0,
    {},
    set(),
    False,
    # correct type, incorrect form
    [],  # only 1 dimension
    [[]],  # only 2 dimensions
    [  # 3 dimensions, but fails on width
        [[], [], []],
        [[], []],
        [[], [], []],
    ],
    [  # 2.5 dimensions
        [[], [], []],
        ['should', 'be', 'lists'],
        [[], [], []],
    ],
    [  # 2.5 dimensions
        [[], [], []],
        'should be 2D list',
        [[], [], []],
    ],
    [  # 3 dimensions, but fails on incorrect type
        [[], [], []],
        [[], [1], []],
        [[], [], []],
    ],
]


@mark.parametrize('template', poor_templates)
def test_is_valid_template_error_detection(template):
    valid, err_msg = _is_valid_template(template)

    assert not valid, F"Assumed valid: {template=}"
    assert err_msg != "", "No helpful error message"


@mark.parametrize('template', poor_templates)
def test_produce_ansi_field_sad_path(template):
    with raises(TypeError):
        produce_ansi_field(template)
