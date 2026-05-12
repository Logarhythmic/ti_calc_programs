import math

try:
    import ti_plotlib as plt  # type: ignore[import-not-found]
except Exception:
    plt = None

# Swap this function out for any other complex-valued function f(x).
# Placeholder: Binet closed form for Fibonacci extension.
# f(x) = (PHI^x - PSI^x) / sqrt(5)
SQRT5 = math.sqrt(5)
PHI = (1 + SQRT5) / 2
PSI = (1 - SQRT5) / 2


def psi_power(x):
    # Principal branch: psi = |psi| * exp(i*pi), so psi^x = |psi|^x * exp(i*pi*x).
    mag = (-PSI) ** x
    ang = math.pi * x
    return mag * math.cos(ang), mag * math.sin(ang)


def f(x):
    psi_re, psi_im = psi_power(x)
    re = (PHI ** x - psi_re) / SQRT5
    im = -psi_im / SQRT5
    return re, im


# Domain and sampling controls
X_MIN = -8.0
X_MAX = 8.0
SAMPLES = 220

def split_re_im(value):
    if isinstance(value, tuple) or isinstance(value, list):
        if len(value) >= 2:
            return value[0], value[1]

    try:
        return value.real, value.imag
    except Exception:
        return float(value), 0.0


def sample_parts(func, x_min, x_max, samples):
    xs = []
    re_vals = []
    im_vals = []

    if samples < 2:
        samples = 2

    step = (x_max - x_min) / (samples - 1)

    for i in range(samples):
        x = x_min + i * step
        z = func(x)
        re, im = split_re_im(z)
        xs.append(x)
        re_vals.append(re)
        im_vals.append(im)

    return xs, re_vals, im_vals


def auto_bounds(values):
    y_min = min(values)
    y_max = max(values)

    if y_min == y_max:
        y_min -= 1.0
        y_max += 1.0

    # Add margin so curves do not touch borders.
    pad = 0.1 * (y_max - y_min)
    return y_min - pad, y_max + pad


def try_call(name_list, arg_sets):
    for name in name_list:
        fn = getattr(plt, name, None)
        if fn is None:
            continue

        for args in arg_sets:
            try:
                fn(*args)
                return True
            except TypeError:
                continue
            except Exception:
                # Keep trying other compatible names/signatures.
                continue

    return False


def clear_plot():
    try_call(("cls", "clear", "clf"), [()])


def set_window(x_min, x_max, y_min, y_max):
    ok = try_call(
        ("window", "set_window"),
        [
            (x_min, x_max, y_min, y_max),
            ((x_min, x_max, y_min, y_max),),
        ],
    )
    if not ok:
        try_call(("auto_window",), [()])


def set_series_color(name_hint):
    if name_hint == "real":
        candidates = [
            ("red",),
            (255, 0, 0),
            (1,),
        ]
    else:
        candidates = [
            ("blue",),
            (0, 0, 255),
            (2,),
        ]

    try_call(("color", "set_color", "pencolor"), candidates)


def plot_series(xs, ys):
    ok = try_call(
        ("plot_xy", "plotxy", "plot", "scatter"),
        [
            (xs, ys),
            (list(xs), list(ys)),
        ],
    )

    if ok:
        return

    # Fallback: connect points with line-like APIs if list plotting is unavailable.
    for i in range(len(xs) - 1):
        x1, y1 = xs[i], ys[i]
        x2, y2 = xs[i + 1], ys[i + 1]
        if not try_call(("line", "draw_line"), [
            (x1, y1, x2, y2),
            ((x1, y1), (x2, y2)),
        ]):
            break


def show_plot():
    try_call(("show_plot", "show", "display"), [()])


def main():
    if plt is None:
        print("ti_plotlib module not found")
        print("Run this on TI Python")
        return

    xs, re_vals, im_vals = sample_parts(f, X_MIN, X_MAX, SAMPLES)
    x_min, x_max = auto_bounds(re_vals)
    y_min, y_max = auto_bounds(im_vals)

    clear_plot()
    set_window(x_min, x_max, y_min, y_max)

    set_series_color("real")
    plot_series(re_vals, im_vals)

    show_plot()

    print("Parametric plot of (Re[f(x)], Im[f(x)])")
    print("x:[" + str(round(x_min, 3)) + ", " + str(round(x_max, 3)) + "]")
    print("y:[" + str(round(y_min, 3)) + ", " + str(round(y_max, 3)) + "]")


main()
