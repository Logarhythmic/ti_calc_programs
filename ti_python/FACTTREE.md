# FACTTREE - Factor Tree + Prime Factorization (TI Python)

## Description

A TI Python program for TI-84 Plus CE Python calculators that:

- accepts an integer greater than 1
- shows its prime factorization in compact form (example: `12=2^2*3`)
- displays a factor tree built by repeatedly splitting by the smallest divisor
- supports vertical scrolling with arrow keys for long trees

Controls:

- Up arrow: scroll up
- Down arrow: scroll down
- ENTER or CLEAR: exit

## Code

```python
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
```

## How It Works

1. `factor_chain` repeatedly finds the smallest divisor of the current value.
2. Each split is recorded as a pair `(factor, quotient)` for tree display.
3. The list of prime factors is compressed into exponent form like `2^3*3^2`.
4. The display is rendered in an 8-row window:
- row 1 is the prime factorization title
- rows 2-8 show a scrollable section of the tree
5. `get_key()` handles navigation with Up/Down and exits on ENTER/CLEAR.

## Test Inputs

| Input | Prime Factorization | Chain of Splits |
|------:|---------------------|-----------------|
| 12 | `12=2^2*3` | `12 -> 2 6 -> 2 3` |
| 72 | `72=2^3*3^2` | `72 -> 2 36 -> 2 18 -> 2 9 -> 3 3` |
| 97 | `97=97` | prime only (no split rows) |
| 360 | `360=2^3*3^2*5` | `360 -> 2 180 -> 2 90 -> 2 45 -> 3 15 -> 3 5` |
