import cv2
import tkinter as tk
from tkinter import filedialog

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;*.png")])
    if file_path:
        image = cv2.imread(file_path)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

root = tk.Tk()
root.title("OpenCV Image Reader")
root.geometry("300x350")
root.resizable(width=False,height=False)

open_button = tk.Button(root, text="Open Image",background="yellow", command=open_image)
open_button.pack(side="top",padx=5,pady=10)


root.mainloop()
