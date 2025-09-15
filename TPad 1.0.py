import tkinter as tk
from tkinter import filedialog

def create_bare_bones_notepad():
    """
    Creates a minimalist notepad application with only a 'Save' function.
    """
    root = tk.Tk()
    root.title("TerminalPad (Bare-Bones)")

    # Define colors
    bg_color = "#000000"  # Black
    fg_color = "#00FF00"  # Green
    menu_bg = "#333333"  # Dark gray
    menu_fg = "#FFFFFF"  # White

    # Create the text widget
    text_area = tk.Text(
        root,
        bg=bg_color,
        fg=fg_color,
        insertbackground=fg_color,
        font=("Courier New", 12),
        wrap="word"
    )
    text_area.pack(expand=True, fill="both")

    # --- Save Functionality ---

    def save_file():
        """Saves the current text content to a file."""
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            content = text_area.get(1.0, tk.END)
            with open(filepath, "w") as file:
                file.write(content)

    # --- Menu and Shortcut ---

    menu_bar = tk.Menu(root, bg=menu_bg, fg=menu_fg)
    file_menu = tk.Menu(menu_bar, tearoff=0, bg=menu_bg, fg=menu_fg)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)
    
    root.config(menu=menu_bar)
    root.bind("<Control-s>", lambda event: save_file())

    root.mainloop()

if __name__ == "__main__":
    create_bare_bones_notepad()