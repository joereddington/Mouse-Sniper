import tkinter as tk
import pyautogui
from PIL import ImageTk, Image

minx=0
miny=0
(maxx,maxy)=pyautogui.size()

def move_mouse(): 
#moves mouse to the middle of the x's and y's 
    x=(maxx+minx)/2
    y=(maxy+miny)/2
    pyautogui.moveTo(x,y)

def get_screenshot():
    img = pyautogui.screenshot(region=(minx,miny,maxx-minx,maxy-miny))#because the last two are heigh and width
    img = img.resize((400, 225), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

root = tk.Tk()
root.geometry("400x225")

img = get_screenshot()
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def update_screen(e):
    move_mouse()
    img2 = get_screenshot()
    panel.configure(image=img2)
    panel.image = img2

def reset(e):
    global minx,maxx,miny,maxy
    minx=0
    miny=0
    (maxx,maxy)=pyautogui.size()
    update_screen(e)
    

def key_pressed(e):
    global minx,maxx,miny,maxy
    height=maxy-miny
    new_height=height/3
    width=maxx-minx
    new_width=width/3
    print(e.char)
    if (e.char in "123"):
        miny=miny+new_height+new_height
    if (e.char in "456"):
        miny=miny+new_height
        maxy=maxy-new_height
    if (e.char in "789"):
        maxy=maxy/3
    if (e.char in "741"):
        maxx=minx+new_width
    if (e.char in "852"):
        minx=minx+new_width
        maxx=maxx-new_width
    if (e.char in "963"):
        minx=minx+((maxx-minx)/3*2)
    update_screen(e)


def click(e): 
    print("clicked") 
    pyautogui.click()
    pyautogui.click()#clicking twice because the first makes the target application active. 

root.bind("<Return>", click)
root.bind("1", key_pressed)
root.bind("2", key_pressed)
root.bind("3", key_pressed)
root.bind("4", key_pressed)
root.bind("5", key_pressed)
root.bind("6", key_pressed)
root.bind("7", key_pressed)
root.bind("8", key_pressed)
root.bind("9", key_pressed)
root.bind("0", reset)
root.mainloop()

# https://stackoverflow.com/a/3482156/170243 was extremely useful. 
