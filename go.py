import tkinter as tk
import pyautogui
from PIL import ImageTk, Image


def show_imge():
    image_window = tk.Tk()
    img = ImageTk.PhotoImage(pyautogui.screenshot())
    panel = tk.Label(image_window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.mainloop()

show_imge() 
