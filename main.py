import tkinter as tk
from tkinter import ttk
import subprocess
import os
import sys

TOOLS = {
    "📸 Open Camera & Capture (.adipix)": "camera.py",
    "🖼️ Convert PNG/JPG to .adipix": "converter.py",
    "👁️ View .adipix Images": "viewer.py"
}

def launch_tool(script_name):
    python_exec = sys.executable
    subprocess.Popen([python_exec, script_name])

def create_main_ui():
    root = tk.Tk()
    root.title("ADIPIX Toolbox")
    root.geometry("440x300")
    root.configure(bg="#1e1e1e")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton',
                    font=('Segoe UI', 12),
                    background='#3a7ff6',
                    foreground='white',
                    padding=10)
    style.map('TButton', background=[('active', '#5599ff')])
    style.configure('TLabel',
                    background='#1e1e1e',
                    foreground='white',
                    font=('Segoe UI', 11))

    title = ttk.Label(root, text="🎛️ ADIPIX Main Menu", font=("Segoe UI", 15, "bold"))
    title.pack(pady=(30, 20))

    for label, script in TOOLS.items():
        btn = ttk.Button(root, text=label, command=lambda s=script: launch_tool(s))
        btn.pack(pady=8, padx=20, fill='x')

    hint = ttk.Label(root, text="A custom toolkit for .adipix format image capture & viewing.")
    hint.pack(pady=(20, 10))

    root.mainloop()

if __name__ == "__main__":
    create_main_ui()
