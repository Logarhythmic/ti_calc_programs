# CPXFPLOT

## Description

Plots a complex-valued function by sampling over a real x-domain, then graphing the parametric curve:

- x = Re(f(x))
- y = Im(f(x))

The default placeholder function is Binet's closed-form Fibonacci extension:

f(x) = (PHI^x - PSI^x) / sqrt(5)

where:

- PHI = (1 + sqrt(5)) / 2
- PSI = (1 - sqrt(5)) / 2

You can replace f(x) at the top of the program with any complex-valued function.

## Implementation Notes

- Uses only math and ti_plotlib modules.
- Computes fractional powers of PSI via Euler form:
  psi^x = |psi|^x * (cos(pi*x) + i*sin(pi*x))
- Samples x on [X_MIN, X_MAX], extracts Re(f(x)) and Im(f(x)), and plots the complex-plane curve (Re(f(x)), Im(f(x))).
- Includes compatibility calls for ti_plotlib function-name differences across firmware versions.

## File

See the latest source in CPXFPLOT.py.
