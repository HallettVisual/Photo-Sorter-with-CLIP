# PhotoSorter

A GUI application to sort and copy photos using OpenAI's CLIP model.

## Description

PhotoSorter uses OpenAI's CLIP model to analyze and categorize your photos based on their content. It provides a user-friendly graphical interface to select a directory of photos and specify categories for sorting.

## Features

- GUI interface built with Tkinter.
- Customize categories for sorting.
- Supports `.jpg`, `.jpeg`, and `.png` image formats.
- Uses GPU acceleration if available.

## Installation

### Prerequisites

- **Python 3.7 or higher** installed on your system.
  - Download from [python.org](https://www.python.org/downloads/).
  - **Windows Users**: During installation, make sure to check the box **"Add Python to PATH"**.
- **pip** package installer (comes with Python).
- **Git** (optional, for cloning the repository).
  - Download from [git-scm.com](https://git-scm.com/downloads).

### Clone the Repository

#### Option 1: Using Git

```bash
git clone https://github.com/YourUsername/PhotoSorter.git
cd PhotoSorter
```

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

#### For Unix/Linux/Mac Users

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

### Create the "Photo Sorter Start.bat" File (For Windows Users)

Create a batch file named **`Photo Sorter Start.bat`** in the `PhotoSorter` folder with the following content:

```batch
@echo off
cd /d "%~dp0"
python photo_sorter.py
pause
```

- **Instructions**:

  - Open Notepad.
  - Copy and paste the content above.
  - Save the file as **`Photo Sorter Start.bat`** in the `PhotoSorter` folder.
  - Make sure to select **"All Files (\*.\*)"** in the **Save as type** dropdown.

## Usage

### For Windows Users

- Start the application by running:

  - Double-click on **`Photo Sorter Start.bat`** in the `PhotoSorter` folder.

### For Unix/Linux/Mac Users

- Run the application:

  ```bash
  python3 photo_sorter.py
  ```

## Steps to Use the Application

1. **Select Directory**: Click on **"Select Directory"** to choose the folder containing your photos.
2. **Enter Categories**: Input the categories you want to sort your photos into, separated by commas.
   - Default categories: `Nature, People, Animals, Urban, Others`
3. **Sort Photos**: Click on **"Sort Photos"** to start the sorting process.
4. **Result**: Photos will be copied into folders named after the specified categories within the selected directory.

## Example

- **Categories**: `Beach, Mountains, City, Forest, Desert`
- **After Sorting**: The selected directory will contain folders named `Beach`, `Mountains`, etc., with the photos sorted accordingly.

## Dependencies

- **Python Libraries**:

  - `torch`
  - `clip` (OpenAI's CLIP)
  - `Pillow`
  - `ftfy`
  - `regex`
  - `tqdm`

- **Hardware**:

  - A CUDA-enabled GPU is recommended for faster processing but not required.

## Troubleshooting

- **No GUI Appears**:

  - Ensure all dependencies are installed correctly.
  - Run the application from Command Prompt to see any error messages.

- **ModuleNotFoundError**:

  - Install missing modules using `pip install module_name`.

- **Tkinter Issues**:

  - Tkinter is included with standard Python installations.
  - If you encounter issues, ensure Python is correctly installed and that Tkinter is included.

- **Permission Errors**:

  - Run the script with appropriate permissions or as an administrator.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI CLIP](https://github.com/openai/CLIP)
- [PyTorch](https://pytorch.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

## Contact

- **Author**: Your Name
- **Email**: your.email@example.com

---

You can now copy and paste this entire README into your `README.md` file.
