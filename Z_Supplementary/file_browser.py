from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import os

def browse_image():

	home_dir = os.path.expanduser("~")

	file_path = filedialog.askopenfilename(
		initialdir=home_dir,
		filetypes = [("Image Files","*.png *.jpg *.jpeg")]
	)

	if not file_path:
		return

	img = Image.open(file_path)
	img = img.resize((250, 250), Image.Resampling.LANCZOS)

	tk_img = ImageTk.PhotoImage(img)

	image_label.config(image=tk_img)
	image_label.image = tk_img


root = Tk()

root.title("Image Visual")
root.geometry("500x500")

frm = ttk.Frame(root, padding=10)
frm.pack(fill=BOTH, expand=True)

browse_btn = ttk.Button(frm, text="Browse Image", command=browse_image)
browse_btn.pack(pady=10)

image_label = Label(frm)
image_label.pack(pady=10)

root.mainloop()