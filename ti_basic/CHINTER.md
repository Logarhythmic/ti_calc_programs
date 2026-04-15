# CHINTER — Chi-Squared Confidence Interval

## Description

A TI Basic program that calculates a chi-squared confidence interval for a population variance and standard deviation, given a confidence level, degrees of freedom, and sample standard deviation. Draws the shaded region on the χ² distribution curve, then displays the variance and standard deviation intervals.

Enter the program line by line using the `PRGM` button on your calculator.

## Code

```
Input "CONFIDENCE?",P
Input "DF?",D
Input "STD DEV?",S
(1-P)/2→R
(1-P)/2+P→L
solve(1-χ²cdf(0,X,D)-R,X,0)→R
solve(1-χ²cdf(0,X,D)-L,X,0)→L

0→Xmin
0→Ymin
1.2*R→Xmax
1.2*χ²pdf((R+L)/2)→Ymax
ClrDraw
Shadeχ²(L,R,D)
Pause

(D)(S^2)/R→M
(D)(S^2)/L→N
√(M)→O
√(N)→P
Disp "LEFT AND RIGHT CHI"
Disp L,R
Disp "PRESS ENTER"
Pause
Disp "VAR INTERVAL"
Disp M,N
Disp "STDEV INTERVAL"
Disp O,P
```

## Test Inputs

Use these values to verify your program is working correctly.

**Example:** 95% confidence, df = 10, s = 3

| Output | Expected value |
|--------|---------------|
| Left χ² | ≈ 3.247 |
| Right χ² | ≈ 20.483 |
| Variance interval | ≈ (4.394, 27.692) |
| Std dev interval | ≈ (2.096, 5.262) |
