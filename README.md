# 🖼️ ADIPIX - All New Image Format

**Bored with JPG, PNG? Try: `adipix` — a custom raw RGB image format.**

---

## 🚀 About

ADIPIX is a new Image Format that stores RAW RGB Values as `.adipix` format.
This repo contains python code in order to create, capture, convert existing jpg/png files into adipix format.

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

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/adipix-viewer.git
   cd adipix-viewer
   
2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

---

##▶️ Usage

1. Run with:

   ```bash
   python main.py

2. The app will open GUI interface to Directly Capture in adipix via camera or covert existing files (jpg/png) or view the adipix files.

Select any file to open and view it.

---

##🧩 Project Structure


    adipix/
    ├── captures/           # Folder to store your .adipix image files
    ├── converter.py        # Converts images to .adipix image file
    ├── camera.py           # Directly Captures image in .adipix format
    ├── main.py             # Main app file - launches the GUI
    ├── viewer.py           # Image loading & viewing logic
    ├── requirements.txt    # Python dependencies
    └── README.md           # You are here!

---

##📄 License

Distributed under the MIT License. See LICENSE for more information.

---

##💬 Contact
Created by Aditya Raj - adityaraj94505@gmail.com <br>
GitHub: [https://github.com/yourusername](https://github.com/devadityaraj) <br>
LinkedIN: [https://www.linkedin.com/in/devadityaraj/](https://www.linkedin.com/in/devadityaraj) <br>

✨ Thank you for checking out ADIPIX Image Viewer! Enjoy your pixel-perfect experience. ✨
