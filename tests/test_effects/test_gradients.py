from pytest import mark

from colour_fx.effects.gradients import create_vertical_gradient


@mark.parametrize('test_name, feed_in, vals, step, ind, expected', [
    (
        # test name
        "normal happy path",
        # feed_in
        [
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
        ],
        # vals
        [[1], [2]],
        # step
        1,
        # indent
        0,
        # expected
        [
            [[1], [1], [1], [2], [2]],
            [[1], [1], [1], [2], [2]],
            [[1], [1], [1], [2], [2]],
            [[1], [1], [1], [2], [2]],
        ],
    ),
    (
        # test name
        "zero step test",
        # feed_in
        [
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
        ],
        # vals
        [[1], [2]],
        # step
        0,
        # indent
        0,
        # expected
        [
            [[1], [1], [1], [2], [2]],
            [[1], [1], [1], [2], [2]],
            [[1], [1], [1], [2], [2]],
            [[1], [1], [1], [2], [2]],
        ],
    ),
    (
        # test name
        "indent test",
        # feed_in
        [
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
        ],
        # vals
        [[1], [2]],
        # step
        1,
        # indent
        1,
        # expected
        [
            [[1], [1], [1], [2], [2]],
            [[1], [1], [2], [2], [2]],
            [[1], [2], [2], [2], [1]],
            [[2], [2], [2], [1], [1]],
        ],
    ),
    (
        # test name
        "reverse indent test",
        # feed_in
        [
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
        ],
        # vals
        [[1], [2]],
        # step
        1,
        # indent
        -1,
        # expected
        [
            [[1], [1], [1], [2], [2]],
            [[2], [1], [1], [1], [2]],
            [[2], [2], [1], [1], [1]],
            [[2], [2], [2], [1], [1]],
        ],
    ),
    (
        # test name
        "step test",
        # feed_in
        [
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
        ],
        # vals
        [[1], [2]],
        # step
        2,
        # indent
        1,
        # expected
        [
            [[1], [1], [1], [2], [2]],
            [[1], [1], [1], [2], [2]],
            [[1], [1], [2], [2], [2]],
            [[1], [1], [2], [2], [2]],
        ],
    ),
    (
        # test name
        "long input vals + indent test",
        # feed_in
        [
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
        ],
        # vals
        [[1], [2], [3], [4], [5], [6], [7]],
        # step
        1,
        # indent
        1,
        # expected
        [
            [[1], [2], [3], [4], [5]],
            [[2], [3], [4], [5], [6]],
            [[3], [4], [5], [6], [7]],
            [[4], [5], [6], [7], [1]],
        ],
    ),
    (
        # test name
        "multiple vals test",
        # feed_in
        [
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
        ],
        # vals
        [[1, 2, 3], [4, 5, 6]],
        # step
        1,
        # indent
        1,
        # expected
        [
            [[1, 2, 3], [1, 2, 3], [1, 2, 3], [4, 5, 6], [4, 5, 6]],
            [[1, 2, 3], [1, 2, 3], [4, 5, 6], [4, 5, 6], [4, 5, 6]],
            [[1, 2, 3], [4, 5, 6], [4, 5, 6], [4, 5, 6], [1, 2, 3]],
            [[4, 5, 6], [4, 5, 6], [4, 5, 6], [1, 2, 3], [1, 2, 3]],
        ],
    ),
    (
        # test name
        "text template test",
        # feed_in
        "\n\nvalid\n",
        # vals
        [[1], [2], [3], [4], [5], [6], [7]],
        # step
        1,
        # indent
        1,
        # expected
        [
            [[1], [2], [3], [4], [5]],
            [[2], [3], [4], [5], [6]],
            [[3], [4], [5], [6], [7]],
            [[4], [5], [6], [7], [1]],
        ],
    ),
])
def test_create_vertical_gradient(
    test_name,
    feed_in,
    vals,
    step,
    ind,
    expected
):
    got = create_vertical_gradient(
        template=feed_in,
        ansi_vals=vals,
        step=step,
        indent=ind
    )

    assert got == expected, (
        F"test: '{test_name}' failed\n"
        F"got: {got}\n"
        F"expected: {expected}"
    )
