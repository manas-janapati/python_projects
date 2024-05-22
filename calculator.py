import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)
        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root)
        display_frame.pack(expand=True, fill='both')

        display_label = tk.Label(display_frame, textvariable=self.result_var, font=("Arial", 24), anchor='e', bg='white', fg='black')
        display_label.pack(expand=True, fill='both')

        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill='both')

        # Button layout
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '',
            '1', '2', '3', '-', '',
            '0', '.', '=', '+', ''
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            if button != '':
                btn = tk.Button(button_frame, text=button, font=("Arial", 18), command=lambda b=button: self.on_button_click(b))
                btn.grid(row=row_val, column=col_val, sticky='nsew')

            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
        elif button == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += button
        self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
