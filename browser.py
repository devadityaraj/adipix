import tkinter as tk
from tkinter import filedialog, messagebox, Scrollbar, Listbox, RIGHT, Y, LEFT, BOTH, END, Frame, Label, Button
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

class AdipixBrowser:
    def __init__(self, root):
        self.root = root
        self.current_path = os.path.join(os.path.expanduser("~"), "Pictures", "Adipix")
        self.root.title("ADIPIX File Browser")
        self.root.configure(bg="#1e1e1e")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        self.title = Label(root, text="ADIPIX File Browser", bg="#1e1e1e", fg="#ffffff", font=("Segoe UI", 18, "bold"))
        self.title.pack(pady=(20, 5))

        self.path_label = Label(root, text=self.current_path, bg="#1e1e1e", fg="#aaaaaa", font=("Segoe UI", 10))
        self.path_label.pack(pady=(0, 10))

        self.choose_btn = Button(root, text="Open Folder", font=("Segoe UI", 10, "bold"),
                                 command=self.choose_folder, bg="#3a7ff6", fg="white",
                                 activebackground="#5a9fff", bd=0, padx=10, pady=5)
        self.choose_btn.pack(pady=(0, 10))

        self.frame = Frame(root, bg="#1e1e1e")
        self.frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox = Listbox(self.frame, yscrollcommand=self.scrollbar.set,
                               font=("Segoe UI", 12), bg="#2e2e2e", fg="#eeeeee",
                               selectbackground="#3a7ff6", selectforeground="#ffffff",
                               activestyle="none", relief="flat", bd=0,
                               highlightthickness=0)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)

        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        self.listbox.bind("<Motion>", self.on_motion)
        self.update_file_list(self.current_path)

    def choose_folder(self):
        folder = filedialog.askdirectory(initialdir=self.current_path)
        if folder:
            self.current_path = folder
            self.path_label.config(text=folder)
            self.update_file_list(folder)

    def update_file_list(self, path):
        self.listbox.delete(0, END)
        try:
            items = sorted(f for f in os.listdir(path)
                           if os.path.isfile(os.path.join(path, f)) and f.lower().endswith(".adipix"))

            if not items:
                self.listbox.insert(END, "(No .adipix files found)")
                self.listbox.config(state="disabled")
                return

            self.listbox.config(state="normal")
            for i, file in enumerate(items):
                self.listbox.insert(END, file)
                self.listbox.itemconfig(i, bg="#3a3a3a" if i % 2 == 0 else "#2e2e2e")
        except Exception as e:
            messagebox.showerror("Error", f"Could not access folder:\n{e}")

    def on_select(self, event):
        selection = event.widget.curselection()
        if not selection:
            return
        index = selection[0]
        selected = self.listbox.get(index)

        if selected == "(No .adipix files found)":
            return

        full_path = os.path.join(self.current_path, selected)
        show_adipix_image(full_path)

    def on_motion(self, event):
        widget = event.widget
        index = widget.nearest(event.y)
        widget.selection_clear(0, END)
        widget.selection_set(index)

def main():
    root = tk.Tk()
    app = AdipixBrowser(root)
    root.mainloop()

if __name__ == "__main__":
    main()
