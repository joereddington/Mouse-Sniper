import tkinter as tk
import pyautogui
from PIL import ImageTk, Image

def get_screenshot():
    img = pyautogui.screenshot()
    img = img.resize((400, 225), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

root = tk.Tk()
root.geometry("400x225")

img = get_screenshot()
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback(e):
    img2 = get_screenshot()
    panel.configure(image=img2)
    panel.image = img2

root.bind("<Return>", callback)
root.mainloop()


# https://stackoverflow.com/a/3482156/170243 was extremely useful. 
