from colour_fx.four_bit import Colour
from colour_fx import compile_ansi_code

RESET = compile_ansi_code()
red = compile_ansi_code(Colour.RED)
orange = compile_ansi_code(Colour.RED.bright)
yellow = compile_ansi_code(Colour.YELLOW.bright)
green = compile_ansi_code(Colour.GREEN)
blue = compile_ansi_code(Colour.BLUE)
indigo = compile_ansi_code(Colour.BLUE.bright)
violet = compile_ansi_code(Colour.MAGENTA.bright)


print(F"{red}         ::::::::      :::       :::   :::   :::::::::  :::        :::::::::: {RESET}")  # r
print(F"{orange}       :+:    :+:   :+: :+:    :+:+: :+:+:  :+:    :+: :+:        :+:         {RESET}")  # o
print(F"{yellow}      +:+         +:+   +:+  +:+ +:+:+ +:+ +:+    +:+ +:+        +:+          {RESET}")  # y
print(F"{green}     +#++:++#++ +#++:++#++: +#+  +:+  +#+ +#++:++#+  +#+        +#++:++#      {RESET}")  # g
print(F"{blue}           +#+ +#+     +#+ +#+       +#+ +#+        +#+        +#+            {RESET}")  # b
print(F"{indigo}   #+#    #+# #+#     #+# #+#       #+# #+#        #+#        #+#             {RESET}")  # i
print(F"{violet}   ########  ###     ### ###       ### ###        ########## ##########       {RESET}")  # v