import tkinter as tk
from tkinter import messagebox, Scrollbar, Listbox, RIGHT, Y, LEFT, BOTH, END, Frame, Label
from PIL import Image, ImageTk
import os

CAPTURES_DIR = "captures"

def load_adipix(filename):
    with open(filename, 'rb') as f:
        if f.read(4) != b'ADPX':
            raise ValueError("Invalid .adipix file")
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        data = list(f.read(width * height * 3))
        pixels = [(data[i], data[i+1], data[i+2]) for i in range(0, len(data), 3)]
        return width, height, pixels

def show_adipix_image(filename):
    try:
        width, height, pixels = load_adipix(filename)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image:\n{e}")
        return

    img = Image.new("RGB", (width, height))
    img.putdata(pixels)

    viewer = tk.Toplevel()
    viewer.title(f"ADIPIX Viewer - {os.path.basename(filename)}")
    viewer.configure(bg="#2e2e2e")
    viewer.geometry(f"{width}x{height}+{center_x(viewer, width)}+{center_y(viewer, height)}")
    viewer.resizable(False, False)

    border = Frame(viewer, bg="#444444", padx=3, pady=3)
    border.pack(padx=10, pady=10)

    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(border, image=tk_img, bg="#2e2e2e")
    label.image = tk_img 
    label.pack()

def center_x(win, width):
    return (win.winfo_screenwidth() // 2) - (width // 2)

def center_y(win, height):
    return (win.winfo_screenheight() // 2) - (height // 2)

def list_adipix_files():
    if not os.path.exists(CAPTURES_DIR):
        os.makedirs(CAPTURES_DIR)
    files = [f for f in os.listdir(CAPTURES_DIR) if f.lower().endswith(".adipix")]
    return files

def on_file_select(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        filename = event.widget.get(index)
        full_path = os.path.join(CAPTURES_DIR, filename)
        show_adipix_image(full_path)

def on_listbox_motion(event):
    widget = event.widget
    index = widget.nearest(event.y)
    widget.selection_clear(0, END)
    widget.selection_set(index)

def main():
    root = tk.Tk()
    root.title("ADIPIX Viewer - Select file")
    root.configure(bg="#1e1e1e")

    width, height = 500, 600
    screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)

    title = Label(root, text="Select an .adipix File", bg="#1e1e1e", fg="#ffffff", font=("Segoe UI", 18, "bold"))
    title.pack(pady=(20, 10))

    frame = Frame(root, bg="#1e1e1e")
    frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(frame, yscrollcommand=scrollbar.set,
                      font=("Segoe UI", 12), bg="#2e2e2e", fg="#eeeeee",
                      selectbackground="#3a7ff6", selectforeground="#ffffff",
                      activestyle="none", relief="flat", bd=0,
                      highlightthickness=0)
    listbox.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    files = list_adipix_files()
    if not files:
        listbox.insert(END, "No .adipix files found in 'captures/'")
        listbox.config(state='disabled')
    else:
        for i, file in enumerate(files):
            listbox.insert(END, file)
            if i % 2 == 0:
                listbox.itemconfig(i, bg="#3a3a3a")
            else:
                listbox.itemconfig(i, bg="#2e2e2e")

    listbox.bind("<<ListboxSelect>>", on_file_select)
    listbox.bind("<Motion>", on_listbox_motion)

    root.mainloop()

if __name__ == "__main__":
    main()
