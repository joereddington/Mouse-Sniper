import tkinter as tk
import pyautogui
from PIL import ImageTk, Image


def show_imge():
    image_window = tk.Tk()
    image_window.geometry("400x225")
    img = pyautogui.screenshot()
    img = img.resize((400, 225), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(image_window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.after(1000,keyboard_stuff)
    image_window.mainloop()



def keyboard_stuff():
    import keyboard 
    while True: 
       if keyboard.read_key() == "p":
            print("you pressed p") 
            continue
show_imge() 
