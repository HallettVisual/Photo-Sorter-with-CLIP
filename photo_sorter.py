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
