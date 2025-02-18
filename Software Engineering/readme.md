# Weather Modeling Project Testing Using Selenium

## Project Overview
This project focuses on developing and testing weather models using Selenium. It provides an interactive interface for solving quadratic equations as part of the weather model calculations and evaluates functionality through automated testing.

## Features
- **Quadratic Solver Web Application**: An HTML-based tool for solving quadratic equations.
- **Testing Suite**: An experimental Selenium notebook for automated testing of the quadratic solver's features.
- **Input Methods**:
  - Hard-coded variables
  - Keyboard input
  - Reading from a file
  - Single set of input
  - Multiple sets of input
- **Graphical Visualization**: Generates graphs of quadratic equations using Plotly.

## Files
### 1. `quadratic_solver.html`
This file contains the HTML and JavaScript code for the quadratic solver application. Users can:
- Solve equations using different input methods.
- Visualize quadratic functions with an interactive graph.

### 2. `Exp2_selenium_testing.ipynb`
A Jupyter Notebook containing Selenium tests to validate the functionalities of `quadratic_solver.html`. The tests include:
- Checking hardcoded and user-provided inputs.
- Verifying file upload functionality.
- Ensuring correct graph generation.

### 3. `coefficients.txt`
A sample input file for testing the file upload feature. It contains sets of coefficients for quadratic equations in the format:
```
a b c
```
Example:
```
4 -7 3
5 -1 4
3 6 4
```

## Requirements
- **Python 3.x**
- **Selenium**: For automated browser testing.
- **Jupyter Notebook**: For running the Selenium tests.
- **Plotly**: For graph generation.
- **Web Browser**: Preferably Google Chrome or Mozilla Firefox.

## Usage
### Running the Quadratic Solver
1. Open `quadratic_solver.html` in your web browser.
2. Choose an input method (e.g., hardcoded, keyboard, or file).
3. Enter coefficients or upload a file.
4. Click "Solve" to view results and graph.

### Running Tests
1. Open the Jupyter Notebook `Exp2_selenium_testing.ipynb`.
2. Ensure Selenium is installed and set up with the appropriate WebDriver.
3. Execute the notebook cells to run tests on the quadratic solver.

## Author
**Janapati Venkata Sri Veda Manaswi**
