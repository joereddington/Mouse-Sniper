import tkinter as tk
import copy
from configparser import ConfigParser
from tkinter  import PhotoImage 
import time
import pyautogui
from PIL import ImageTk, Image, ImageDraw


class Box: 

    def __init__(self):
        self.minx=0
        self.miny=0
        (self.maxx,self.maxy)=pyautogui.size()

    @property
    def x(self):
        return (self.maxx+self.minx)/2 

    @property
    def y(self):
        return (self.maxy+self.miny)/2

    def process_num_key(self, e):
        height=self.maxy-self.miny
        new_height=int(height/3)
        width=self.maxx-self.minx
        new_width=int(width/3)
        if new_width<3:
            print("Maximum Zoom level reached")
            return
        print("Before({}) :{}<x<{},{}<y<{}".format(e.char,self.minx,self.maxx,self.miny,self.maxy))
        if (e.char in "123"):
            self.miny=self.miny+new_height+new_height
        if (e.char in "456"):
            self.miny=self.miny+new_height
            self.maxy=self.maxy-new_height
        if (e.char in "789"):
            self.maxy=self.miny+new_height
        if (e.char in "741"):
            self.maxx=self.minx+new_width
        if (e.char in "852"):
            self.minx=self.minx+new_width
            self.maxx=self.maxx-new_width
        if (e.char in "963"):
            self.minx=self.minx+new_width+new_width
        print("After ({}):{}<x<{},{}<y<{},new_width,new_height".format(e.char,self.minx,self.maxx,self.miny,self.maxy))

vp=Box() 

#TODO: MAYBE should be global 
stored_x=0
stored_y=0
ori_img=pyautogui.screenshot()
input_queue=[]


def move_mouse(): 
    pyautogui.moveTo(vp.x,vp.y)

def update_image():
    global ori_img
    global vp
    img=ori_img.crop((vp.minx,vp.miny,vp.maxx,vp.maxy))
    img=draw_grid(img)
    return ImageTk.PhotoImage(img)

def draw_grid(img, colour="red"):
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

def update_screen():
    move_mouse()
    img = update_image()
    panel.configure(image=img)
    panel.image = img

def reset_numbers():
    global vp 
    vp=Box()

def reset(e):
    #This doesn't reset stored and possible should? 
    reset_numbers()
    ori_img = pyautogui.screenshot()
    update_screen()
    
def back(e):
    input_queue.pop()
    process_queue(input_queue)

def process_queue(input_queue):
    reset_numbers()
    for x in input_queue:
        vp.process_num_key(x)
    update_screen()

def num_key_pressed(e): 
    input_queue.append(e) 
    chars=[e.char for e in input_queue]
    print(chars)
    process_queue(input_queue)






def drag(e):
    global stored_x, stored_y
    print(stored_x)
    # Store the co-ordinate
    stored_x=vp.x
    sotred_y=vp.y
    print("Co-ordinates stored") 

def click(e): 
    global stored_x, stored_y
    print(stored_x) #TODO: NO bare prints
    if stored_x > 0: #If there was a co-ordinate stored.
        print("Executing Drag") 
        # TODO, put in the drag  
        #now reset them.  
        pyautogui.moveTo(stored_x,stored_y)
        duration=1 
        pyautogui.dragTo(vp.x,vp.y,duration,button='left')
        stored_x=0
        stored_y=0
    else:
        print("clicked") 
        clickwrapper(e)
        reset(e)
    input_queue=[]

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


def bind_keys(root):
    root.bind("<KP_Enter>", doubleclick) #TODO: it would be good if we could press enter a few times rather than having separate buttons
    root.bind("+", click)
    root.bind("-", drag)
    for x in range(9):
        root.bind(str(x+1),num_key_pressed)
    root.bind("0", back)
    root.bind("s", save)
    root.bind("S", save)
    root.bind("<FocusIn>", on_focus_in) #TODO: what does this do? 

if __name__ == "__main__":
    config=ConfigParser()
    config.read('ms.ini')
    print("Clicks so far: {}".format(config.get('main','clicks')))

    root = tk.Tk()
    root.title("Mouse Sniper")
    root.geometry("800x450+1600+50")#this is hardcoded and shouldn't be
    img = update_image()
    panel = tk.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    bind_keys(root)
    root.mainloop()
#TODO: <UP><DOWN> and so on should move the window slightly
#TODO: should be a 'repeat position' option. Presumably the multiply * 
#TODO: tidy up for a code review.
# https://stackoverflow.com/a/3482156/170243 was extremely useful. 
# https://stackoverflow.com/questions/46567324/tkinter-window-focus-loss-event 
# TODO - reset should would back thorugh a stack (of inputs
