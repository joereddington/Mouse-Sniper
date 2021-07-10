import tkinter as tk
from configparser import ConfigParser
from tkinter  import PhotoImage 
import time
import pyautogui
from PIL import ImageTk, Image, ImageDraw

minx=0
miny=0
stored_x=0
stored_y=0
(maxx,maxy)=pyautogui.size()
ori_img=pyautogui.screenshot()


def move_mouse(): 
    x=(maxx+minx)/2
    y=(maxy+miny)/2
    pyautogui.moveTo(x,y)

def update_image():
    global ori_img
    global minx,maxx,miny,maxy
    (height,width)=pyautogui.size()
    img=ori_img.crop((minx,miny,maxx,maxy))
    img=draw_grid(img)
    return ImageTk.PhotoImage(img)

def draw_grid(img):
    colour="red"
    win_height=800
    win_width=450
    img = img.resize((win_height, win_width), Image.ANTIALIAS)
    draw= ImageDraw.Draw(img)
    for x in range(1,9):
        draw.line((win_height/9*x,0,win_height/9*x,win_width),fill="blue", width=2)
    for x in range(1,9):
        draw.line((0,win_width/9*x,win_height,win_width/9*x),fill="blue", width=2)
    draw.line((win_height/3,0,win_height/3,win_width),fill=colour, width=3)
    draw.line((win_height/3*2,0,win_height/3*2,win_width),fill=colour, width=3)
    draw.line((0,win_width/3*2,win_height,win_width/3*2),fill=colour, width=3)
    draw.line((0,win_width/3,win_height,win_width/3),fill=colour, width=3)
    return img

def update_screen(e):
    move_mouse()
    img = update_image()
    panel.configure(image=img)
    panel.image = img


def reset(e):
    #This doesn't reset stored and possible should? 
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

def drag(e):
    global stored_x, stored_y
    print(stored_x)
    # Store the co-ordinate
    stored_x=(maxx+minx)/2
    stored_y=(maxy+miny)/2
    print("Co-ordinates stored") 

def click(e): 
    global stored_x, stored_y
    print(stored_x)
    if stored_x > 0: #If there was a co-ordinate stored.
        print("Executing Drag") 
        # TODO, put in the drag  
        #now reset them.  
        pyautogui.moveTo(stored_x,stored_y)
        x=(maxx+minx)/2
        y=(maxy+miny)/2
        duration=1 
        pyautogui.dragTo(x,y,duration,button='left')
        
        stored_x=0
        stored_y=0
    else:
        print("clicked") 
        clickwrapper(e)
        reset(e)

def save(e): 
    fp="/Users/Shared/git/screenshot.png"
    print("Saving to {}".format(fp))
    img=ori_img.crop((minx,miny,maxx,maxy))
    img.save(fp)


def clickwrapper(e):
    clicks=int(config.get('main','clicks'))
    pyautogui.click()
    clicks=clicks+1
    config.set('main','clicks',str(clicks))
    print("Clicks is now: {}".format(clicks))
    with open('ms.ini', 'w') as f:
        config.write(f)

def doubleclick(e): 
    print("doubleclicked") 
    clickwrapper(e)
    time.sleep(0.4)
    clickwrapper(e)#clicking twice because the first makes the target application active. 
    reset(e)

def on_focus_in(e): 
    print("We have focus!") 
    reset(e) 



config=ConfigParser()
config.read('ms.ini')
print("Clicks so far: {}".format(config.get('main','clicks')))

root = tk.Tk()
root.title("Mouse Sniper")
root.geometry("800x450+1600+50")#this is hardcoded and shouldn't be
img = update_image()
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.bind("<KP_Enter>", doubleclick)
root.bind("+", click)
root.bind("-", drag)
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
root.bind("s", save)
root.bind("S", save)
root.bind("<FocusIn>", on_focus_in)
root.mainloop()

# https://stackoverflow.com/a/3482156/170243 was extremely useful. 
# https://stackoverflow.com/questions/46567324/tkinter-window-focus-loss-event 

