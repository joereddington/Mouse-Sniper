import tkinter as tk
import pyautogui
from PIL import ImageTk, Image

minx=0
miny=0
(maxx,maxy)=pyautogui.size()
ori_img=0


def move_mouse(): 
#moves mouse to the middle of the x's and y's 
    x=(maxx+minx)/2
    y=(maxy+miny)/2
    pyautogui.moveTo(x,y)

def get_screenshot():
    global ori_img
    ori_img = pyautogui.screenshot()
    img = ori_img.resize((400, 225), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img


def update_image():
    global ori_img
    global minx,maxx,miny,maxy
    (height,width)=pyautogui.size()
    img=ori_img.crop((minx,miny,maxx,maxy))
    img = img.resize((400, 225), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img


def update_screen(e):
    move_mouse()
    img2 = update_image()
    panel.configure(image=img2)
    panel.image = img2


def reset(e):
    global minx,maxx,miny,maxy
    minx=0
    miny=0
    (maxx,maxy)=pyautogui.size()
    update_screen(e)
    get_screenshot()#refreshes the ori_img
    
def key_pressed(e):
    global minx,maxx,miny,maxy
    height=maxy-miny
    new_height=int(height/3)
    width=maxx-minx
    new_width=int(width/3)
    if new_width<3:
        print("Don't want to zoom more")
        return
    if new_height<3:
        print("Don't want to zoom more")
        return
    print("{}: {},{},{},{}".format(e.char,minx,maxx,miny,maxy))
    if (e.char in "123"):
        miny=miny+new_height+new_height
    if (e.char in "456"):
        miny=miny+new_height
        maxy=maxy-new_height
    if (e.char in "789"):
        maxy=int(maxy/3)
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
    get_screenshot()#refreshes the ori_img


root = tk.Tk()
root.geometry("400x225")
img = get_screenshot()
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.bind("<KP_Enter>", click)
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
