import tkinter as tk
import pyautogui
from PIL import ImageTk, Image

minx=0
miny=0
(maxx,maxy)=pyautogui.size()

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
    img2 = get_screenshot()
    panel.configure(image=img2)
    panel.image = img2



def left():
    global minx,maxx
    width=maxx-minx
    new_width=width/3
    maxx=minx+new_width
    
def right():
    global minx,maxx
    #maxx stays, minx changes 
    minx=minx+((maxx-minx)/3*2)

def ahead():
    global minx,maxx
    width=maxx-minx
    new_width=width/3
    minx=minx+new_width
    maxx=maxx-new_width

def top():
    global maxy
    maxy=maxy/3

def middle(): 
    global miny,maxy
    height=maxy-miny
    new_height=height/3
    miny=miny+new_height
    maxy=maxy-new_height

def bottom():
    global miny,maxy
    height=maxy-miny
    new_height=height/3
    miny=miny+new_height+new_height

     
def nine(e):
    right()
    top()
    update_screen(e)

def eight(e):
    top()
    middle()
    update_screen(e)

def seven(e): 
    left()
    top()
    update_screen(e)

def six(e):
    right()
    middle()
    update_screen(e)

def five(e): 
    ahead()
    middle()
    update_screen(e)

def four(e):
    left()
    middle()
    update_screen(e)


def three(e):
    right()
    bottom()
    update_screen(e)

def two(e): 
    ahead()
    bottom()
    update_screen(e)

def one(e):
    left()
    bottom()
    update_screen(e)


def reset(e):
    global minx,maxx,miny,maxy
    minx=0
    miny=0
    (maxx,maxy)=pyautogui.size()
    update_screen(e)
    

root.bind("<Return>", update_screen)
root.bind("1", one)
root.bind("2", two)
root.bind("3", three)
root.bind("4", four)
root.bind("5", five)
root.bind("6", six)
root.bind("7", seven)
root.bind("8", eight)
root.bind("9", nine)
root.bind("-", reset)
root.mainloop()

# https://stackoverflow.com/a/3482156/170243 was extremely useful. 
