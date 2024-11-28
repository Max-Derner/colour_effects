from typing import Union

from colour_fx._util import ansi_field, ansi_val_collection
from colour_fx.effects._fx_util import (
    produce_ansi_field,
    stretch_ansi_val_collection
)


def create_vertical_gradient_field(
        template: Union[str, ansi_field],
        ansi_vals: ansi_val_collection,
        *,
        step: int = 1,
        indent: int = 0,
) -> ansi_field:
    step = step or 1  # can't have 0 step
    field = produce_ansi_field(template)
    field_height = len(field)
    field_width = len(field[0])
    ansi_vals = stretch_ansi_val_collection(field_width, ansi_vals)

    for line_no in range(field_height):
        if line_no != 0 and line_no % step == 0:
            ansi_vals = ansi_vals[indent:] + ansi_vals[:indent]
        for col_no in range(field_width):
            field[line_no][col_no].extend(ansi_vals[col_no])

    return field


def create_horizontal_gradient_field(
        template: Union[str, ansi_field],
        ansi_vals: ansi_val_collection,
        *,
        step: int = 1,
        indent: int = 0,
) -> ansi_field:
    field = produce_ansi_field(template)
    field_height = len(field)
    field_width = len(field[0])
    ansi_vals = stretch_ansi_val_collection(field_height, ansi_vals)

    array_bias = []
    for col_no in range(field_width):
        step_no = col_no // step
        array_bias.append(step_no * indent)

    for line_no in range(field_height):
        for col_no in range(field_width):
            code_idx = (line_no + array_bias[col_no]) % len(ansi_vals)
            field[line_no][col_no].extend(ansi_vals[code_idx])
    return field
