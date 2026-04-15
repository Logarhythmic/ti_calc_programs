# TI Basic Programs

This folder contains programs written in TI Basic for TI-83/84 series calculators.

## File Types

- **`.md`** — Markdown documentation for each program, including a description, full source code, explanation of how it works, and test inputs.
- **`.8xp`** — Compiled program files ready to be sent to a calculator. Use [TI Connect CE](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw) (or a similar transfer tool) to load these onto your calculator.

## Transferring Programs to Your Calculator

1. Download or locate the `.8xp` file you want.
2. Connect your calculator to your computer via USB.
3. Open TI Connect CE, then drag and drop the `.8xp` file onto your calculator.

The program will appear in the calculator's program menu (`PRGM`) and can be run from there.

## Contributing

If you'd like to contribute a program, please include a `.md` file alongside any `.8xp` file. The markdown file should follow this structure:

```markdown
# PROGRAMNAME — Short Human-Readable Title

## Description

A brief explanation of what the program does and any relevant context (e.g., which calculator models it targets, whether a built-in alternative exists, how to enter it on the calculator).

## Code

\```
(paste the TI Basic source code here)
\```

## How It Works

(Optional) A deeper explanation of the algorithm, inputs, outputs, and internal variable usage. Useful for longer or more complex programs.

## Test Inputs

A table or list of sample inputs and their expected outputs so users can verify the program was entered correctly.
```
