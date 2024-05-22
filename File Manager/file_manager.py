import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python File Manager")
        self.root.geometry("800x600")
        
        # Set style
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")

        # Define fonts and colors
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12), padding=6)
        self.style.configure("TEntry", font=("Helvetica", 12), padding=6)
        self.style.configure("TListbox", font=("Helvetica", 12))

        self.current_path = os.getcwd()

        # Load icons
        self.refresh_icon = ImageTk.PhotoImage(Image.open("icons/refresh.png").resize((20, 20), Image.LANCZOS))
        self.open_icon = ImageTk.PhotoImage(Image.open("icons/open.png").resize((20, 20), Image.LANCZOS))
        self.delete_icon = ImageTk.PhotoImage(Image.open("icons/delete.png").resize((20, 20), Image.LANCZOS))
        self.create_icon = ImageTk.PhotoImage(Image.open("icons/create.png").resize((20, 20), Image.LANCZOS))
        self.up_icon = ImageTk.PhotoImage(Image.open("icons/up.png").resize((20, 20), Image.LANCZOS))

        self.path_frame = ttk.Frame(root, padding=10)
        self.path_frame.pack(fill=tk.X)

        self.path_label = ttk.Label(self.path_frame, text="Current Path:")
        self.path_label.pack(side=tk.LEFT)

        self.path_entry = ttk.Entry(self.path_frame, width=70)
        self.path_entry.pack(side=tk.LEFT, padx=5)
        self.path_entry.insert(0, self.current_path)

        self.path_frame_buttons = ttk.Frame(self.path_frame)
        self.path_frame_buttons.pack(side=tk.LEFT)

        self.refresh_button = ttk.Button(self.path_frame_buttons, image=self.refresh_icon, command=self.refresh)
        self.refresh_button.pack(side=tk.LEFT, padx=2)

        self.up_button = ttk.Button(self.path_frame_buttons, image=self.up_icon, command=self.go_up)
        self.up_button.pack(side=tk.LEFT, padx=2)

        self.listbox_frame = ttk.Frame(root, padding=10)
        self.listbox_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.listbox_frame, selectmode=tk.SINGLE, font=("Helvetica", 12))
        self.listbox.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(0, 10), pady=5)

        self.scrollbar = ttk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.buttons_frame = ttk.Frame(root, padding=10)
        self.buttons_frame.pack()

        self.open_button = ttk.Button(self.buttons_frame, text="Open", image=self.open_icon, compound=tk.LEFT, command=self.open_item)
        self.open_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Delete", image=self.delete_icon, compound=tk.LEFT, command=self.delete_item)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.create_button = ttk.Button(self.buttons_frame, text="Create File", image=self.create_icon, compound=tk.LEFT, command=self.create_file)
        self.create_button.pack(side=tk.LEFT, padx=5)

        self.refresh()

    def refresh(self):
        self.current_path = self.path_entry.get()
        self.listbox.delete(0, tk.END)
        try:
            items = os.listdir(self.current_path)
            for item in items:
                self.listbox.insert(tk.END, item)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_item(self):
        selected = self.listbox.curselection()
        if selected:
            item = self.listbox.get(selected[0])
            new_path = os.path.join(self.current_path, item)
            if os.path.isdir(new_path):
                self.path_entry.delete(0, tk.END)
                self.path_entry.insert(0, new_path)
                self.refresh()
            else:
                os.startfile(new_path)

    def go_up(self):
        new_path = os.path.dirname(self.current_path)
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, new_path)
        self.refresh()

    def delete_item(self):
        selected = self.listbox.curselection()
        if selected:
            item = self.listbox.get(selected[0])
            path_to_delete = os.path.join(self.current_path, item)
            try:
                if os.path.isdir(path_to_delete):
                    os.rmdir(path_to_delete)
                else:
                    os.remove(path_to_delete)
                self.refresh()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def create_file(self):
        new_file_path = filedialog.asksaveasfilename(initialdir=self.current_path, title="Create New File")
        if new_file_path:
            open(new_file_path, 'w').close()
            self.refresh()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
