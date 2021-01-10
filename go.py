import tkinter as tk
import pyautogui
from PIL import ImageTk, Image, ImageDraw

minx=0
miny=0
(maxx,maxy)=pyautogui.size()
ori_img=pyautogui.screenshot()


def move_mouse(): 
    x=(maxx+minx)/2
    y=(maxy+miny)/2
    pyautogui.moveTo(x,y)

def update_image():
    win_height=400
    win_width=225
    colour="red"
    global ori_img
    global minx,maxx,miny,maxy
    (height,width)=pyautogui.size()
    img=ori_img.crop((minx,miny,maxx,maxy))
    img = img.resize((win_height, win_width), Image.ANTIALIAS)
    draw= ImageDraw.Draw(img)
    draw.line((win_height/3,0,win_height/3,win_width),fill=colour, width=3)
    draw.line((win_height/3*2,0,win_height/3*2,win_width),fill=colour, width=3)
    draw.line((0,win_width/3*2,win_height,win_width/3*2),fill=colour, width=3)
    draw.line((0,win_width/3,win_height,win_width/3),fill=colour, width=3)
    img = ImageTk.PhotoImage(img)
    return img


def update_screen(e):
    move_mouse()
    img = update_image()
    panel.configure(image=img)
    panel.image = img


def reset(e):
    global minx,maxx,miny,maxy,ori_img
    minx=0
    miny=0
    (maxx,maxy)=pyautogui.size()
    ori_img = pyautogui.screenshot()
    update_screen(e)
    
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
    print("{}:{}<x<{},{}<y<{},new_width,new_height".format(e.char,minx,maxx,miny,maxy))
    if (e.char in "123"):
        miny=miny+new_height+new_height
    if (e.char in "456"):
        miny=miny+new_height
        maxy=maxy-new_height
    if (e.char in "789"):
        maxy=miny+new_height
    if (e.char in "741"):
        maxx=minx+new_width
    if (e.char in "852"):
        minx=minx+new_width
        maxx=maxx-new_width
    if (e.char in "963"):
        minx=minx+new_width+new_width
    print("Now {}:{}<x<{},{}<y<{},new_width,new_height".format(e.char,minx,maxx,miny,maxy))
    update_screen(e)

def click(e): 
    print("clicked") 
    pyautogui.click()
    reset(e)

def doubleclick(e): 
    print("doubleclicked") 
    pyautogui.click()
    pyautogui.click()#clicking twice because the first makes the target application active. 
    reset(e)

def on_focus_in(e): 
    print("We have focus!") 
    reset(e) 

root = tk.Tk()
root.wm_attributes("-topmost", 1) #from https://stackoverflow.com/questions/3926655/how-to-keep-a-python-window-on-top-of-all-others-python-3-1
root.title("Mouse Sniper")
root.geometry("400x225+0+800")#this is hardcoded and shouldn't be
img = update_image()
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.bind("<KP_Enter>", doubleclick)
root.bind("+", click)
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
root.bind("<FocusIn>", on_focus_in)
root.mainloop()

# https://stackoverflow.com/a/3482156/170243 was extremely useful. 
# https://stackoverflow.com/questions/46567324/tkinter-window-focus-loss-event 

