import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk

def show_image():
    image_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;*.png")])
    if image_path:
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV uses BGR, convert it to RGB
    
    # Convert the image to PIL format
    image_pil = Image.fromarray(image)
    
    # Convert PIL image to Tkinter PhotoImage
    photo = ImageTk.PhotoImage(image_pil)
    
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

root = tk.Tk()
root.title("Image Viewer")



button = tk.Button(root, text="Show Image", command=show_image)
button.pack()

root.mainloop()