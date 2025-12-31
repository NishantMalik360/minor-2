# Zlatan ASCII Art Generator

A Python project that converts image files (specifically of Zlatan Ibrahimovic) into ASCII art text. This project demonstrates core programming concepts including loop iteration, conditional logic, file handling, and basic image processing using the PIL (Pillow) library.

## 📖 Project Purpose

The primary goal of this project is to apply fundamental Python skills to a creative engineering problem. It bridges the gap between abstract concepts (arrays, loops, conditionals) and visual output.

**Key Concepts Applied:**
* **Loops:** Iterating through image data (pixels) and string construction.
* **Conditionals/Logic:** Mapping pixel brightness (0-255) to specific ASCII characters based on density.
* **Data Structures:** Using Lists to store character maps.
* **File I/O:** Reading images and writing text output to files.

---

## ⚙️ How It Works

The algorithm follows a 4-step pipeline:

1.  **Resize:** The original image is resized to a manageable width (e.g., 100 pixels). The height is adjusted to account for the aspect ratio of terminal characters (which are taller than they are wide), typically using a factor of 0.55.
2.  **Grayscale Conversion:** The image is converted to "L" mode (Luminance), discarding color information. This leaves us with pixels ranging from 0 (Black) to 255 (White).
3.  **Mapping:** Each pixel value is divided by 25 to find its corresponding index in our ASCII character list (e.g., `["@", "#", ... , "."]`). Dark pixels map to dense characters (`@`), and light pixels map to sparse characters (`.`).
4.  **Rendering:** The resulting list of characters is sliced into lines matching the new image width and printed to the console or saved to a text file.

---

## 🚀 How to Run the Program

### Prerequisites
* Python 3.x installed.
* `Pillow` library installed.

### Installation Steps
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/zlatan-ascii.git](https://github.com/YOUR_USERNAME/zlatan-ascii.git)
    cd zlatan-ascii
    ```

2.  **Install dependencies:**
    ```bash
    pip install pillow
    ```

3.  **Prepare your image:**
    * Place your desired image in the project folder.
    * Rename it to `zlatan.jpg` (or update the filename in the code).

4.  **Run the script:**
    ```bash
    python ascii_art.py
    ```

5.  **View Output:**
    * The ASCII art will appear in your terminal.
    * A file named `zlatan_output.txt` will be generated in the folder.

---

## 🔌 Integration Guide (How to use this in other projects)

This script is designed to be modular. You can use the ASCII conversion logic in other Python applications (e.g., a Discord bot, a web app, or a CLI tool).

### Step 1: File Structure
Ensure `ascii_art.py` is in the same directory as your new project file, or in your Python path.

```text
/My_New_Project
│
├── main_app.py       <-- Your new program
├── ascii_art.py      <-- This script (the library)
└── assets/
    └── player.jpg

Step 2: Import and Use
In your main_app.py, import the convert_image_to_ascii function.

# main_app.py

# 1. Import the function from our module
from ascii_art import convert_image_to_ascii

# 2. Define the path to your image
image_path = "assets/player.jpg"

# 3. Call the function
# You can optionally specify a width (default is 100)
ascii_result = convert_image_to_ascii(image_path, new_width=120)

# 4. Use the result
if ascii_result:
    print("--- Player Stats Loaded ---")
    print(ascii_result)
else:
    print("Error loading image.")
