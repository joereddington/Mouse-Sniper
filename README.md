# Mouse-Sniper
Fast keyboard control of mouse


This script is based off the concept of [Quick Mouse](https://github.com/trishume/QuickMouse). I wanted to write my own because the original wasn't something I was capable of maintaining without learning ruby, and I fancied a quick project for the Xmas break. 

The use case is: use your keyboards numberpad to replace a mouse for the occasional click. I've written this more for my own personal sport than for accessibility purposes, but accessibility is in the back of my mind. 

When the script is started, a preview window is shown. At the start, the preview window shows the whole screen. The preview window is split into nine zones, the nine zones are labeled according to the layout of keys on the numberpad. 

When one of the numberpad keys is pressed, then the mouse moves to the centre of the targeted section and the preview window zooms in on that section, pressing another numberpad key refines the location until the desired target is under the cursor. At this point, you can press return to click. 

At any point, press '-' to reset the zoom.    


# TODO 
* Multiple monitor support
* double click, drag, second click ect 
* Click in the preview window. 
* Keep the application selected
* Zoom out one level  
* proper 3 by 3 overlay in the preview window
* Improve speed - cache the screenshot for example. 
* settings page: always on top? preview window off? 
* Option to automatically focus on window
* Hotkey to start
* put into stackexchange code review. 
* refactor a whole lot.        
* Fix the 'tile cannot extend outside image' bug.  
