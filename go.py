import tkinter as tk
import keyboard 
import pyautogui
from PIL import ImageTk, Image

image_window = tk.Tk()

def get_screenshot():
    img = pyautogui.screenshot()
    img = img.resize((400, 225), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

def show_imge():
    image_window.geometry("400x225")
    panel = tk.Label(image_window, image=get_screenshot())
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.after(1000,keyboard_stuff)
    image_window.mainloop()

def keyboard_stuff():
    while True: 
       if keyboard.read_key() == "p":
            print("you pressed p") 
            panel = tk.Label(image_window, image=get_screenshot())
            panel.pack(side="bottom", fill="both", expand="yes")
            continue

show_imge() 
