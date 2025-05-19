import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os

def save_adipix(img, path):
    img = img.convert('RGB')
    width, height = img.size
    pixels = list(img.getdata())

    with open(path, 'wb') as f:
        f.write(b'ADPX')  # Custom header
        f.write(width.to_bytes(4, 'little'))
        f.write(height.to_bytes(4, 'little'))
        for r, g, b in pixels:
            f.write(bytes([r, g, b]))

def convert_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if not file_path:
        return

    try:
        img = Image.open(file_path)

        save_dir = "captures"
        os.makedirs(save_dir, exist_ok=True)

        base_name = os.path.basename(file_path)
        name_without_ext = os.path.splitext(base_name)[0]
        output_path = os.path.join(save_dir, name_without_ext + ".adipix")

        save_adipix(img, output_path)
        messagebox.showinfo("Success", f"Converted and saved as:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert:\n{str(e)}")


def create_ui():
    root = tk.Tk()
    root.title("ADIPIX Image Converter")
    root.geometry("600x500")
    root.configure(bg="#121212")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton',
                    font=('Segoe UI', 12),
                    background='#3a7ff6',
                    foreground='white',
                    padding=10)
    style.map('TButton', background=[('active', '#5599ff')])

    style.configure('TLabel',
                    background='#121212',
                    foreground='white',
                    font=('Segoe UI', 11))

    title_label = ttk.Label(root, text="Convert PNG/JPG to .adipix", font=("Segoe UI", 14, "bold"))
    title_label.pack(pady=(30, 10))

    convert_btn = ttk.Button(root, text="Choose An Image To Convert", command=convert_image)
    convert_btn.pack(pady=10)

    hint_label = ttk.Label(root, text=".adipix is a custom image format with raw RGB data", font=("Segoe UI", 9))
    hint_label.pack(pady=(20, 10))

    root.mainloop()

if __name__ == "__main__":
    create_ui()