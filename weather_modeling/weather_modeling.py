import math
import matplotlib.pyplot as plt

# Function to solve the quadratic equation
def quadratic_solver(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
   
    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        return None

# Function to solve weather-related quadratic equations
def solve_weather_equation(a, b, c):
    solutions = quadratic_solver(a, b, c)
    return solutions

# Function to plot the weather model
def plot_weather_model(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if there are real roots before plotting
    if discriminant >= 0:
        x = range(-4, 4)  # Range of x values
        y = [a * (i**2) + b * i + c for i in x]  # Calculate y values based on quadratic equation

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f"{a}x^2 + {b}x + {c}")  # Plot the quadratic function
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.title('Weather Model')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("No real roots. Cannot plot the graph.")

import os

def main():
    choice = input("Choose an option:\n1. Hard-coded variables\n2. Keyboard input\n3. Read from a file\n")

    if choice == '1':
        # Hard-coded coefficients
        a = 4
        b = -7
        c = 3
        solutions = solve_weather_equation(a, b, c)
        print("Solutions:", solutions)
        plot_weather_model(a, b, c)
       
    elif choice == '2':
        # Take coefficients from user input
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        solutions = solve_weather_equation(a, b, c)
        print("Solutions:", solutions)
        plot_weather_model(a, b, c)
       
    elif choice == '3':
        # Allow user to enter the full file path or use default path
        default_file_path = r"C:\Users\manas\Desktop\weather_modelling\coefficients.txt"
        print(f"Using default file path: {default_file_path}")
        
        filename = input(f"Enter the filename (or press Enter to use default path {default_file_path}): ")
        
        # If the user doesn't provide a filename, use the default path
        if filename.strip() == "":
            filename = default_file_path
        
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    coefficients = list(map(float, line.split()))
                    if len(coefficients) == 3:
                        a, b, c = coefficients
                        solutions = solve_weather_equation(a, b, c)
                        print(f"Coefficients: {coefficients} -> Solutions: {solutions}")
                        plot_weather_model(a, b, c)
                    else:
                        print(f"Skipping invalid line: {line}")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please provide a valid file name or path.")
        except ValueError:
            print("Error reading coefficients from file. Ensure the file contains numbers only.")
       
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# main function
if __name__ == "__main__":
    main()
