# INVT — Inverse t-CDF

## Description

A TI Basic program that calculates the inverse t-CDF (i.e., the t-value corresponding to a given left-tail area) given a degrees of freedom and left-tail area. Useful for finding critical values when constructing confidence intervals or performing hypothesis tests.

> **Note:** Newer TI calculators have this function built in. This program is specifically for older TI-83 models that lack a built-in `invT`.

Enter the program line by line using the `PRGM` button on your calculator.

## Code

```
Input "LEFT AREA?",A
Input "DF?",D
solve(A-tcdf(-10^99,X,D),X,0)→T
Disp T
```

## Test Inputs

Use these values to verify your program is working correctly.

| Left Area (A) | Degrees of Freedom (D) | Expected Result |
|---------------|------------------------|-----------------|
| 0.9 | 25 | ≈ 1.316345073 |
| 0.8 | 35 | ≈ 0.8520118881 |
| 0.99 | 7 | ≈ 2.997951566 |
