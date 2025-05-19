# 🖼️ ADIPIX Image Viewer

**A modern, lightweight GUI application to view `.adipix` — a custom raw RGB image format.**

---

## 🚀 About

ADIPIX Image Viewer lets you easily browse and view images saved in the custom `.adipix` format. It features:

- Smooth, native Tkinter GUI with a dark, stylish theme  
- Automatic file listing from a `captures/` directory  
- Dynamic image resizing to fit screen resolution without distortion  
- Simple, intuitive interface optimized for ease of use  
- Cross-platform support (Windows, macOS, Linux)

---

## 📸 What is `.adipix`?

`.adipix` is a custom image format created to store raw RGB pixel data efficiently, with a minimal 12-byte header:

| Header | Description          |
|--------|----------------------|
| `ADPX` | Magic signature (4B) |
| Width  | Image width (4B)     |
| Height | Image height (4B)    |

Pixels follow as raw RGB triplets.

---

## 🎯 Features

- **Browse all `.adipix` files** in the `captures/` folder  
- **Click to view** any image in a separate window  
- **Smart scaling**: if image resolution exceeds screen size, it scales down proportionally  
- **Clean UI**: dark mode with crisp typography and colors  
- **Error handling** for corrupted or invalid files  
- Portable and minimal dependencies (Python + Pillow + Tkinter)

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/adipix-viewer.git
   cd adipix-viewer
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Usage
Run the viewer with:

bash
Copy
Edit
python main.py
The app will scan the captures/ folder for .adipix files and display them in a list.

Select any file to open and view it.

Images larger than your screen will automatically resize to fit.

🧩 Project Structure
bash
Copy
Edit
adipix-viewer/
├── captures/           # Folder to store your .adipix image files
├── main.py             # Main app file - launches the GUI
├── viewer.py           # Image loading & viewing logic
├── requirements.txt    # Python dependencies
└── README.md           # You are here!
⚙️ How to Create .adipix Files
You can create .adipix images from PNG or JPG using the custom converter (see converter.py):

Reads an image

Converts to raw RGB with the ADPX header

Saves as .adipix

👥 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check issues page.

📄 License
Distributed under the MIT License. See LICENSE for more information.

💬 Contact
Created by Your Name - your.email@example.com
GitHub: https://github.com/yourusername

✨ Thank you for checking out ADIPIX Image Viewer! Enjoy your pixel-perfect experience. ✨
