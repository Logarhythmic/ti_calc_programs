# TI Basic Programs

A collection of small programs written for TI-83/84 series graphing calculators.

## Repository Structure

- **`ti_basic/`** — Programs written in TI Basic (the built-in programming language on TI-83/84 calculators).
  - `.md` files contain human-readable documentation: description, source code, how it works, and test inputs.
  - `.8xp` files are the compiled program files that can be transferred directly to a calculator using [TI Connect CE](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw) or similar tools.
- **`ti_python/`** — Programs written in TI Python (for calculators that support the Python app, such as the TI-84 Plus CE with the Python edition firmware).

## Getting Started

### Loading a program onto your calculator

1. Download the `.8xp` file for the program you want.
2. Connect your TI-83/84 calculator to your computer via USB.
3. Open [TI Connect CE](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw).
4. Drag and drop the `.8xp` file onto your calculator in TI Connect CE.

### Reading the source code

The `.md` files in `ti_basic/` contain the source code for each program in a fenced code block, along with a description, explanation of how it works, and test inputs to verify the program was entered correctly.

## Contributing

Feel free to open an issue or pull request if you have a program to share or an improvement to suggest. When contributing a TI Basic program, please include a `.md` documentation file formatted as described in [`ti_basic/README.md`](ti_basic/README.md).
