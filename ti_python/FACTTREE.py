from ti_system import disp_at, disp_clr, get_key
import math

VISIBLE_ROWS = 8
KEY_UP = 25
KEY_DOWN = 34
KEY_ENTER = 105
KEY_CLEAR = 45


def factor_chain(n):
    smallest = []
    pairs = []
    a = n

    while a > 1:
        f = 0
        limit = int(math.sqrt(a))
        d = 2
        while d <= limit:
            if a % d == 0:
                f = d
                break
            d += 1

        if f == 0:
            smallest.append(a)
            a = 1
        else:
            q = a // f
            smallest.append(f)
            pairs.append((f, q))
            a = q

    return smallest, pairs


def exponent_string(primes):
    if not primes:
        return ""

    parts = []
    current = primes[0]
    exp = 1

    for value in primes[1:] + [None]:
        if value == current:
            exp += 1
        else:
            if exp == 1:
                parts.append(str(current))
            else:
                parts.append(str(current) + "^" + str(exp))
            current = value
            exp = 1

    return "*".join(parts)


def build_tree_lines(n, pairs):
    lines = [str(n)]

    for depth, pair in enumerate(pairs):
        left, right = pair
        lines.append(" " * (3 * depth) + "/\\")
        lines.append(" " * (2 * depth) + str(left) + " " + str(right))

    return lines


def render(lines, top, title):
    disp_clr()
    disp_at(1, 1, title[:26])

    for row in range(VISIBLE_ROWS - 1):
        idx = top + row
        if idx < len(lines):
            disp_at(row + 2, 1, lines[idx][:26])


def main():
    try:
        n = int(input("INTEGER (>1)? "))
    except Exception:
        print("INPUT MUST BE")
        print("AN INTEGER >1")
        return

    if n < 2:
        print("INPUT MUST BE")
        print("AN INTEGER >1")
        return

    primes, pairs = factor_chain(n)
    pf = exponent_string(primes)
    title = str(n) + "=" + pf
    lines = build_tree_lines(n, pairs)

    top = 0
    max_top = max(0, len(lines) - (VISIBLE_ROWS - 1))

    while True:
        render(lines, top, title)

        key = get_key(1)

        if key == KEY_DOWN and top < max_top:
            top += 1
        elif key == KEY_UP and top > 0:
            top -= 1
        elif key == KEY_ENTER or key == KEY_CLEAR:
            break


main()
