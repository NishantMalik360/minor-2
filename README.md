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
    git clone https://github.com/NishantMalik360/minor-2.git
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

## 📂 Project Structure

Ensure `ascii_art.py` is in the same directory as your new project file, or in your Python path.

```text
/My_New_Project
│
├── ascii_art.py
└── player.jpg
```
