from typing import Any, Union, Tuple

from colour_fx import ansi_field


def produce_ansi_field(
        template: Union[str, ansi_field],
        ) -> ansi_field:
    """An ANSI field is a 3 dimensional list of strings. The first
    dimension represents each line of text, the second dimension
    represents each individual character, and the third dimension
    represents to different ANSI values that will be compiled into a
    single ANSI escape sequence for that character.

    Accepts either the text for which you wish to create an ANSI
    field, or a previous ANSI field you want copying"""
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
