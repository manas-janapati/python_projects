# Software Engineering Lab Activity - Weather Modelling

**Author:** Janapati Venkata Sri Veda Manaswi

## Overview
This project is a part of my Software Engineering Lab activity. The main purpose of this program is to solve quadratic equations using the standard formula, plot the corresponding quadratic curve, and provide solutions for real or complex roots based on the equation's discriminant. It also includes a feature to read coefficients from a text file, input them manually, or use predefined coefficients.

## Features:
- **Quadratic Equation Solver:** Solves quadratic equations of the form `ax^2 + bx + c = 0` based on the coefficients.
- **Graph Plotting:** Plots the quadratic equation curve using `matplotlib` based on the given coefficients.
- **Multiple Input Options:**
  - **Hardcoded Variables:** Use predefined coefficients to solve the equation and plot the graph.
  - **Keyboard Input:** Input the coefficients manually and solve the equation.
  - **File Input:** Read coefficients from a file (`coefficients.txt`).

## How to Run:
1. Clone or download the repository to your local machine.
2. Make sure you have Python installed (version 3.6 or higher).
3. Install the necessary libraries:
    ```bash
    pip install matplotlib
    ```
4. Run the Python script:
    ```bash
    python weather_modeling.py
    ```
5. Select one of the following options:
    - Option 1: Use hardcoded coefficients.
    - Option 2: Enter coefficients manually.
    - Option 3: Read coefficients from a file (ensure `coefficients.txt` is in the same directory or provide the full path).

## Example Usage:
- When running option 3, you will be prompted to enter the filename (e.g., `coefficients.txt`).
- The script will then read the coefficients from the file and plot the graph.

## File Format for Input File:
If you choose to read coefficients from a file, ensure the `coefficients.txt` file follows the format below:
4 -7 3 
5 -1 4 
3 6 4

Each line represents the coefficients `a`, `b`, and `c` for a quadratic equation.

## Conclusion:
This program provides a simple yet effective way to solve and visualize quadratic equations. It demonstrates the use of Python for mathematical problem-solving and graphical representation. The ability to take input from multiple sources (hardcoded, user input, or file) makes it flexible for various scenarios.
