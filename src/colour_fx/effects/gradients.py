from colour_fx._util import ansi_field, ansi_val_collection
from colour_fx.effects._fx_util import (
    produce_ansi_field,
    stretch_ansi_val_collection
)


def create_vertical_gradient(
        template: str | ansi_field,
        ansi_vals: ansi_val_collection,
        *,
        step: int = 1,
        indent: int = 0,
) -> ansi_field:
    step = step or 1  # can't have 0 step
    field = produce_ansi_field(template)
    field_height = len(field)
    field_width = len(field[0])
    ansi_codes = stretch_ansi_val_collection(field_width, ansi_vals)

    for line_no in range(field_height):
        if line_no != 0 and line_no % step == 0:
            ansi_codes = ansi_codes[indent:] + ansi_codes[:indent]
        for col_no in range(field_width):
            field[line_no][col_no].extend(ansi_codes[col_no])

    return field
