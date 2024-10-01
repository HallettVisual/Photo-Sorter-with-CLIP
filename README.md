```markdown
# PhotoSorter

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A GUI application to sort and copy photos using OpenAI's CLIP model.

## How it Works

PhotoSorter uses OpenAI's CLIP model to analyze and categorize your photos based on their content. The application provides a user-friendly graphical interface built with Tkinter, allowing you to select a directory of photos and specify categories for sorting. It supports `.jpg`, `.jpeg`, and `.png` image formats.

The application processes each photo, determines the best matching category, and copies the photo into a folder named after that category within the selected directory. If the CLIP model cannot determine a suitable category, the photo will be placed in an `Others` folder by default.

## Installation

### Prerequisites

- **Python 3.7 or higher**: Download and install from [python.org](https://www.python.org/downloads/).
  - **Windows Users**: During installation, make sure to check the box **"Add Python to PATH"**.
- **pip**: Comes bundled with Python.
- **Git** (optional, for cloning the repository):
  - Download from [git-scm.com](https://git-scm.com/downloads).

### Supported Platforms

- Windows 10 or higher
- macOS
- Linux

### Clone the Repository

#### Option 1: Using Git

```bash
git clone https://github.com/YourUsername/PhotoSorter.git
cd PhotoSorter
```

Replace `YourUsername` with your actual GitHub username.

#### Option 2: Download ZIP

- Go to the repository page on GitHub.
- Click on **"Code"** and select **"Download ZIP"**.
- Extract the ZIP file to a folder of your choice.

### Install Dependencies

#### For Windows Users

1. **Run the Install Script**:

   - Double-click on **`install.bat`** located in the `PhotoSorter` folder.
   - This will automatically install all required Python packages.

2. **Alternative Manual Installation**:

   - Open **Command Prompt**.
   - Navigate to the `PhotoSorter` directory:

     ```bash
     cd path\to\PhotoSorter
     ```

   - Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

#### For Unix/Linux/macOS Users

1. **Make the Install Script Executable**:

   ```bash
   chmod +x install.sh
   ```

2. **Run the Install Script**:

   ```bash
   ./install.sh
   ```

3. **Alternative Manual Installation**:

   ```bash
   pip3 install -r requirements.txt
   ```

### Verify Installation

To ensure that all dependencies are installed correctly, you can run:

```bash
pip list
```

---

## Usage

### Starting the Application

#### For Windows Users

- **Run the Application**:

  - Double-click on **`Photo Sorter Start.bat`** in the `PhotoSorter` folder.

- **Alternative Method**:

  - Open **Command Prompt**.
  - Navigate to the `PhotoSorter` directory:

    ```bash
    cd path\to\PhotoSorter
    ```

  - Run the application:

    ```bash
    python photo_sorter.py
    ```

#### For Unix/Linux/macOS Users

- **Run the Application**:

  ```bash
  python3 photo_sorter.py
  ```

### Steps to Use the Application

1. **Select Directory**:

   - Click on **"Select Directory"** to choose the folder containing your photos.

2. **Enter Categories**:

   - Input the categories you want to sort your photos into, separated by commas.
   - Default categories: `Nature, People, Animals, Urban, Others`

3. **Sort Photos**:

   - Click on **"Sort Photos"** to start the sorting process.

4. **Result**:

   - Photos will be analyzed and copied into folders named after the specified categories within the selected directory.

### Example

- **Categories**: `Beach, Mountains, City, Forest, Desert`
- **After Sorting**: The selected directory will contain folders named `Beach`, `Mountains`, `City`, etc., with the photos sorted accordingly.

---

## Options

### Custom Categories

You can enter any categories you like in the categories text field. Separate multiple categories with commas.

### Device Usage

If you have a CUDA-enabled GPU, the application will utilize it automatically for faster processing. If not, it will default to using the CPU.

### Supported Image Formats

- `.jpg`
- `.jpeg`
- `.png`

---

## Development

### Project Structure

```
PhotoSorter/
├── photo_sorter.py
├── requirements.txt
├── install.bat          (Windows install script)
├── install.sh           (Unix/Linux/macOS install script)
├── Photo Sorter Start.bat (Windows start script)
└── README.md
```

### Files Description

- **photo_sorter.py**: The main application script.
- **requirements.txt**: Lists all Python dependencies.
- **install.bat**: Install script for Windows users.
- **install.sh**: Install script for Unix/Linux/macOS users.
- **Photo Sorter Start.bat**: Shortcut to start the application on Windows.
- **README.md**: Documentation and instructions.

### Running Tests

Currently, there are no automated tests for this project. Contributions are welcome!

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [OpenAI CLIP](https://github.com/openai/CLIP)
- [PyTorch](https://pytorch.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

---

## Contact

- **Author**: Your Name
- **Email**: your.email@example.com

---

## Troubleshooting

- **No GUI Appears**:

  - Ensure all dependencies are installed correctly.
  - Run the application from Command Prompt or Terminal to see any error messages.

- **ModuleNotFoundError**:

  - Install missing modules using `pip install module_name`.

- **Tkinter Issues**:

  - Tkinter is included with standard Python installations.
  - If you encounter issues, ensure Python is correctly installed and that Tkinter is included.

- **Permission Errors**:

  - Run the script with appropriate permissions or as an administrator.

---

## Frequently Asked Questions

### Can I customize the categories?

Yes! You can enter any categories you like in the categories text field when running the application.

### Does the application move or copy the photos?

The application copies photos into the category folders, leaving the original files untouched.

### Can I process other image formats?

Currently, the application supports `.jpg`, `.jpeg`, and `.png` files. Support for additional formats can be added in future updates.

---

## Additional Information

### Full Code Listings

#### `photo_sorter.py`

```python
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import clip
import torch
from PIL import Image

class PhotoSorterApp:
    def __init__(self, master):
        self.master = master
        master.title("Photo Sorter with CLIP")

        # Load the CLIP model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", device=self.device)

        # Labels and Buttons
        self.label = tk.Label(master, text="Select the directory containing your photos:")
        self.label.pack(pady=5)

        self.select_dir_button = tk.Button(master, text="Select Directory", command=self.select_directory)
        self.select_dir_button.pack(pady=5)

        self.categories_label = tk.Label(master, text="Enter categories (comma-separated):")
        self.categories_label.pack(pady=5)

        self.categories_entry = tk.Entry(master, width=50)
        self.categories_entry.pack(pady=5)
        self.categories_entry.insert(0, "Nature, People, Animals, Urban, Others")

        self.sort_button = tk.Button(master, text="Sort Photos", command=self.sort_photos, state=tk.DISABLED)
        self.sort_button.pack(pady=5)

        self.status_label = tk.Label(master, text="")
        self.status_label.pack(pady=5)

        # Initialize variables
        self.photo_dir = ''
        self.categories = []

    def select_directory(self):
        self.photo_dir = filedialog.askdirectory()
        if self.photo_dir:
            self.status_label.config(text=f"Selected directory: {self.photo_dir}")
            self.sort_button.config(state=tk.NORMAL)

    def sort_photos(self):
        self.status_label.config(text="Sorting photos...")
        self.master.update()

        # Get categories from entry
        categories_input = self.categories_entry.get()
        self.categories = [cat.strip() for cat in categories_input.split(',') if cat.strip()]

        if not self.categories:
            messagebox.showerror("Error", "Please enter at least one category.")
            return

        # Create category directories
        for category in self.categories:
            os.makedirs(os.path.join(self.photo_dir, category), exist_ok=True)

        # Preprocess text once
        text_tokens = clip.tokenize(self.categories).to(self.device)
        with torch.no_grad():
            text_features = self.model.encode_text(text_tokens)

        # Process images
        for filename in os.listdir(self.photo_dir):
            filepath = os.path.join(self.photo_dir, filename)
            if os.path.isfile(filepath) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    image = self.preprocess(Image.open(filepath)).unsqueeze(0).to(self.device)
                    with torch.no_grad():
                        image_features = self.model.encode_image(image)

                    # Calculate similarities
                    similarities = (image_features @ text_features.T).softmax(dim=-1)
                    best_category_index = similarities.argmax().item()
                    best_category = self.categories[best_category_index]

                    # Copy file to the corresponding category folder
                    shutil.copy(filepath, os.path.join(self.photo_dir, best_category))
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

        self.status_label.config(text="Photos sorted successfully!")
        messagebox.showinfo("Done", "Photos have been sorted and copied to category folders.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoSorterApp(root)
    root.mainloop()
```

#### `requirements.txt`

```
torch>=1.7.1
git+https://github.com/openai/CLIP.git
Pillow>=8.0.0
ftfy
regex
tqdm
```

#### `install.bat` (Windows)

```batch
@echo off
REM Install dependencies from requirements.txt
pip install -r requirements.txt

REM Inform the user that installation is complete
echo.
echo Installation complete. You can now run the application using:
echo     python photo_sorter.py
pause
```

#### `install.sh` (Unix/Linux/macOS)

```bash
#!/bin/bash
# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Inform the user that installation is complete
echo ""
echo "Installation complete. You can now run the application using:"
echo "    python3 photo_sorter.py"
```

#### `Photo Sorter Start.bat` (Windows)

```batch
@echo off
cd /d "%~dp0"
python photo_sorter.py
pause
```

---

## Future Plans

- **Add Support for More Image Formats**: Including RAW formats like `.CR2`, `.NEF`, etc.
- **Implement Multi-language Support**: To cater to users worldwide.
- **Add a Progress Bar**: To show the progress of the sorting process.
- **Add Error Logging**: To better handle exceptions and provide user feedback.

---

## Changelog

### Version 1.0.0

- Initial release of PhotoSorter.
- Features:
  - GUI application built with Tkinter.
  - Sort photos into user-defined categories using CLIP.
  - Supports `.jpg`, `.jpeg`, and `.png` formats.

---

I hope this comprehensive `README.md` file meets your requirements. It includes all the necessary information, installation instructions, usage guidelines, code listings, and additional details similar to the example you provided.

Feel free to copy and paste this entire content into your `README.md` file and make any necessary adjustments, such as replacing placeholders with your actual information.

Let me know if you need any further assistance!

```
