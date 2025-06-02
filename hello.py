import zyjkit.print as c
from zyjkit.print.code import CODES

from zyjkit.print import zprint

if __name__ == '__main__':
    result = []
    for code in CODES:
        line = f'{code:<20}' + getattr(c, code)('Hello World!')
        result.append(line)

        blue = c.blue('Hello World!')
        line2 = f'{code:<20}' + getattr(blue,  code)
        result.append(line2)

    zprint(result)
