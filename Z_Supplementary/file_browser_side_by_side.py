import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

class RGB2GrayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RGB to Grayscale Viewer")
        self.root.geometry("600x350")

        # Load button
        self.btn_load = tk.Button(root, text="Load Image", command=self.load_image, font=("Arial", 12))
        self.btn_load.pack(pady=10)

        # Frame for side-by-side image display
        self.frame_images = tk.Frame(root)
        self.frame_images.pack(padx=10, pady=10, fill="both", expand=True)

        # Left panel: Original RGB
        self.panel_rgb = tk.Frame(self.frame_images)
        self.panel_rgb.pack(side="left", expand=True)

        self.label_rgb_title = tk.Label(self.panel_rgb, text="Original (RGB)", font=("Arial", 12, "bold"))
        self.label_rgb_title.pack()
        self.canvas_rgb = tk.Label(self.panel_rgb)
        self.canvas_rgb.pack()

        # Right panel: Grayscale
        self.panel_gray = tk.Frame(self.frame_images)
        self.panel_gray.pack(side="left", expand=True)

        self.label_gray_title = tk.Label(self.panel_gray, text="Grayscale", font=("Arial", 12, "bold"))
        self.label_gray_title.pack()
        self.canvas_gray = tk.Label(self.panel_gray)
        self.canvas_gray.pack()

    def load_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if not filepath:
            return

        # Load and display RGB
        img_rgb = Image.open(filepath).convert("RGB")
        img_rgb_resized = img_rgb.resize((256, 256))
        self.photo_rgb = ImageTk.PhotoImage(img_rgb_resized)
        self.canvas_rgb.config(image=self.photo_rgb)

        # Convert to grayscale
        img_gray = ImageOps.grayscale(img_rgb)
        img_gray_resized = img_gray.resize((256, 256))
        self.photo_gray = ImageTk.PhotoImage(img_gray_resized)
        self.canvas_gray.config(image=self.photo_gray)

if __name__ == "__main__":
    root = tk.Tk()
    app = RGB2GrayApp(root)
    root.mainloop()
