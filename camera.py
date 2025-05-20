import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import time
import os

CAPTURES_DIR = os.path.join(os.path.expanduser("~"), "Pictures", "Adipix")
os.makedirs(CAPTURES_DIR, exist_ok=True)

def save_adipix(img, path):
    img = img.convert('RGB')
    width, height = img.size
    pixels = list(img.getdata())

    with open(path, 'wb') as f:
        f.write(b'ADPX')
        f.write(width.to_bytes(4, 'little'))
        f.write(height.to_bytes(4, 'little'))
        for r, g, b in pixels:
            f.write(bytes([r, g, b]))

def add_watermark(frame, text="ADIPIX", pos=(10, 470), opacity=0.5, font_scale=1.2, thickness=2):
    overlay = frame.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    x, y = pos
    cv2.putText(overlay, text, (x, y), font, font_scale, (0, 0, 0), thickness + 3, lineType=cv2.LINE_AA)
    cv2.putText(overlay, text, (x, y), font, font_scale, (255, 255, 255), thickness, lineType=cv2.LINE_AA)

    return cv2.addWeighted(overlay, opacity, frame, 1 - opacity, 0)

class AdipixCameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.configure(bg="#121212")
        self.window.geometry("+400+100")

        style = ttk.Style(self.window)
        style.theme_use('clam')
        style.configure('TButton',
                        background='#3a7ff6',
                        foreground='white',
                        font=('Segoe UI', 12, 'bold'),
                        padding=10)
        style.map('TButton',
                  background=[('active', '#5599ff')])

        style.configure('TLabel',
                        background='#121212',
                        foreground='#e0e0e0',
                        font=('Segoe UI', 11))

        if not os.path.exists(CAPTURES_DIR):
            os.makedirs(CAPTURES_DIR)

        self.cap = cv2.VideoCapture(0)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.canvas = tk.Canvas(window, width=self.width, height=self.height, bg="#121212", highlightthickness=0)
        self.canvas.pack(pady=15)

        self.label_info = ttk.Label(window, text="Press SPACEBAR or Capture button to save image")
        self.label_info.pack(pady=(0,10))

        btn_frame = ttk.Frame(window)
        btn_frame.pack(pady=10)

        self.btn_capture = ttk.Button(btn_frame, text="Capture", command=self.capture_image)
        self.btn_capture.pack(side=tk.LEFT, padx=12)

        self.btn_exit = ttk.Button(btn_frame, text="Exit", command=self.close)
        self.btn_exit.pack(side=tk.LEFT, padx=12)

        self.window.bind('<space>', self.handle_space)

        self.delay = 15
        self.update_frame()

        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.window.mainloop()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:

            pos = (10, self.height - 20)
            frame = add_watermark(frame, pos=pos, opacity=0.4, font_scale=1, thickness=2)

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2image))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update_frame)

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)

            filename = f"capture_{int(time.time())}.adipix"
            full_path = os.path.join(CAPTURES_DIR, filename)
            save_adipix(img_pil, full_path)

            messagebox.showinfo("Captured", f"Image saved as:\n{full_path}")
        else:
            messagebox.showerror("Error", "Failed to capture image from camera.")

    def handle_space(self, event):
        self.capture_image()

    def close(self):
        self.cap.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdipixCameraApp(root, "ADIPIX Camera Capture")
