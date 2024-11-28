from typing import Any, Union, Tuple
from math import ceil

from colour_fx._util import ansi_field, compile_ansi_code


def produce_ansi_field(
        template: Union[str, ansi_field],
) -> ansi_field:
    """Accepts either the text for which you wish to create an ANSI
    field, or a previous ANSI field you want copying

    Returns an ANSI field which can then be passed into
    `apply_ansi_field(text, ansi_field)`:

    An ANSI field is a 3 dimensional list of strings that can be put
    in an ANSI escape sequence SGR. The first dimension represents each
    line of text, the second dimension represents each individual
    character, and the third dimension represents different ANSI
    values that will be compiled into a single ANSI escape sequence for
    that character.

    Example:

    ```python
    from colour_fx.four_bit import Colour
    [
        [[Colour.RED], [], [Colour.BLACK, Colour.CYAN.background]],
        [[], [], []],
        [[Colour.BLACK, Colour.CYAN.background], [], [Colour.RED]],
    ]
    ```
    This ANSI field represents a pattern in a 3x3 grid, the top left and
    bottom right corners will have red text and no background. The top
    right and bottom left corners will have black text on a cyan
    background. Everything else will have default rendering.
    """
    valid_template, err_reason = _is_valid_template(template)
    if valid_template:
        if isinstance(template, str):
            split_text = template.split('\n')
            no_lines = len(split_text)
            no_cols = max(
                [len(line) for line in split_text]
            )
            return [
                [[] for _ in range(no_cols)]
                for _ in range(no_lines)
            ]
        if isinstance(template, list):
            return [
                [col.copy() for col in line]
                for line in template
            ]
    err_reason = err_reason or (
        "No reason given, please report."
    )
    err_msg = F"Template is not valid. Reason:\n{err_reason}"
    raise TypeError(err_msg)


def _is_valid_template(obj: Any) -> Tuple[bool, str]:
    """returns `(is_valid: bool, error_message: str)`

    error_message is empty is template is valid"""
    err_msg = ""
    if isinstance(obj, str):
        return True, ""
    else:
        err_msg += "Object is not string\n"
    is_ansi_field, field_err = _is_valid_ansi_field(obj)
    if is_ansi_field:
        return True, ""
    else:
        err_msg += field_err + "\n"
    return False, err_msg


def _is_valid_ansi_field(obj: Any) -> Tuple[bool, str]:
    """returns `(is_valid: bool, error_message: str)`

    Ansi fields must have three dimensions.

    The first dimension must contain lists that are all the same length,
    known as the nominal width.

    The second dimension must contain all lists of any length including
    zero.

    The third dimension must be all strings. These strings should be
    representing values for use in an ANSI escape sequence SGR, but we
    don't valid those values."""
    # check first dimensional list - the individual lines
    if not isinstance(obj, list):
        return False, "Object is not list"
    if len(obj) < 1:
        return False, "Object is 1 dimensional"
    # check second dimensional list - the characters
    nominal_width = len(obj[0])
    for line_no in range(len(obj)):
        if not isinstance(obj[line_no], list):
            return False, F"No second dimension at index [{line_no}]"
        if len(obj[line_no]) < 1 or len(obj[line_no]) != nominal_width:
            err_msg = (
                F"Incorrect width at index [{line_no}]: expected "
                F"{nominal_width}, got {len(obj[line_no])}"
            )
            return False, err_msg
        # check third dimensional list - the ANSI vals
        for col_no in range(len(obj[line_no])):
            if not isinstance(obj[line_no][col_no], list):
                err_msg = F"No third dimension at index [{line_no}][{col_no}]"
                return False, err_msg
            # check items in lowest depth list are strings
            for idx, value in enumerate(obj[line_no][col_no]):
                if not isinstance(value, str):
                    err_msg = (
                        F"None string ANSI value found at index "
                        F"[{line_no}][{col_no}][{idx}]: "
                        F"{type(value)=}, {value=}"
                    )
                    return False, err_msg
    return True, ""


def apply_ansi_field(
        text: str,
        field: ansi_field,
) -> str:
    lines_of_text = text.split('\n')
    output = ''
    current_ansi_vals = None
    RESET = compile_ansi_code()
    for line_no, line in enumerate(lines_of_text):
        line_no = line_no % len(field)
        column_details = field[line_no]
        for idx, char in enumerate(line):
            idx = idx % len(column_details)
            if current_ansi_vals != (new_vals := column_details[idx]):
                current_ansi_vals = new_vals
                escape_sequence = compile_ansi_code(*current_ansi_vals)
                if escape_sequence == RESET:
                    output += (
                        RESET
                        + char
                    )
                else:
                    output += (
                        RESET
                        + escape_sequence
                        + char
                    )
            else:
                output += char
        output += RESET + '\n'
        current_ansi_vals = None
    return output


def stretch_ansi_val_collection(
        array_length: int,
        ansi_vals: list[str],
) -> list[str]:
    """expands a list of ANSI code value to a new length such that any
    value appearing before another value in the original list will not
    appear after that value in the new list.

    Example:

    `[1, 2, 3]` with new length `6` gives `[1, 1, 2, 2, 3, 3]`

    An intentional quirk is that each element of the original
    `ansi_vals` will be repeated the same amount and so returned list
    may be longer than requested. This is to give uniformity when used
    in conjunction with sloped gradients.

    Example:
    `[1, 2]` with new length `3` gives `[1, 1, 2, 2]`"""
    colour_length = ceil(array_length / len(ansi_vals))
    return [
        ansi_code
        for ansi_code in ansi_vals
        for _ in range(colour_length)
    ]
