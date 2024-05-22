import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Function to generate a random lucky color
def generate_lucky_color():
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple']
    return random.choice(colors)

# Function to generate a random lucky number
def generate_lucky_number():
    return random.randint(1, 100)

def predict_lucky_color_and_number():
    # Get user's name
    user_name = simpledialog.askstring("Input", "Enter your name:", parent=root)
    if not user_name:
        return

    # Predict lucky color and number
    lucky_color = generate_lucky_color()
    lucky_number = generate_lucky_number()

    messagebox.showinfo("Prediction", f"Hello {user_name}! Your lucky color is {lucky_color} and your lucky number is {lucky_number}.")

# Create tkinter window
root = tk.Tk()
root.title("Lucky Predictor")
root.geometry("1000x365")

# Load background image
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame to hold the input and button
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Button to predict lucky color and number
predict_button = tk.Button(frame, text="Predict Lucky Color and Number", command=predict_lucky_color_and_number)
predict_button.pack()

root.mainloop()
