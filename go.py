import tkinter as tk
import pyautogui
from PIL import ImageTk, Image

minx=0
miny=0
(maxx,maxy)=pyautogui.size()

def get_screenshot():
    print(minx,miny,maxx,maxy)
    img = pyautogui.screenshot(region=(minx,miny,maxx,maxy))
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

def zoom(e): 
    print("five was pressed") 
    global minx,maxx,miny,maxy
    new_minx=minx+((maxx-minx)/3)
    new_miny=miny+((maxy-miny)/3)
    new_maxx=maxx-((maxx-minx)/3)
    new_maxy=maxy-((maxy-miny)/3)
    (minx,miny,maxx,maxy)= (new_minx,new_miny,new_maxx,new_maxy)
    callback(e)

root.bind("<Return>", callback)
root.bind("5", zoom)
root.mainloop()


# https://stackoverflow.com/a/3482156/170243 was extremely useful. 
