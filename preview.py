import sys
import tkinter as tk
from tkinter import messagebox, Frame, Label
from PIL import Image, ImageTk
import os

def load_adipix(filename):
    with open(filename, 'rb') as f:
        if f.read(4) != b'ADPX':
            raise ValueError("Invalid .adipix file")
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        data = list(f.read(width * height * 3))
        pixels = [(data[i], data[i+1], data[i+2]) for i in range(0, len(data), 3)]
        return width, height, pixels

def center_x(win, width):
    return (win.winfo_screenwidth() // 2) - (width // 2)

def center_y(win, height):
    return (win.winfo_screenheight() // 2) - (height // 2)

def show_adipix_image(filename):
    try:
        width, height, pixels = load_adipix(filename)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image:\n{e}")
        return

    img = Image.new("RGB", (width, height))
    img.putdata(pixels)

    viewer = tk.Tk()
    viewer.title(f"ADIPIX Viewer - {os.path.basename(filename)}")
    viewer.configure(bg="#2e2e2e")
    viewer.geometry(f"{width}x{height}+{center_x(viewer, width)}+{center_y(viewer, height)}")
    viewer.resizable(False, False)

    border = Frame(viewer, bg="#444444", padx=3, pady=3)
    border.pack(padx=10, pady=10)

    tk_img = ImageTk.PhotoImage(img)
    label = Label(border, image=tk_img, bg="#2e2e2e")
    label.image = tk_img 
    label.pack()

    viewer.mainloop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: adipix_viewer.py <filename.adipix>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        sys.exit(1)

    show_adipix_image(filename)
