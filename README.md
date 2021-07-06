# Mouse-Sniper
Fast keyboard control of mouse

This script is based off the concept of [Quick Mouse](https://github.com/trishume/QuickMouse). I wanted to write my own because the original wasn't something I was capable of maintaining without learning ruby, and I fancied a quick project for the Xmas break. 

The use case is: use your keyboards numberpad to replace a mouse for the occasional click. I've written this more for my own personal sport than for accessibility purposes, but accessibility is in the back of my mind. 

When the script is started, a preview window is shown. At the start, the preview window shows the whole screen. The preview window is split into nine zones, the nine zones are labeled according to the layout of keys on the numberpad. 

When one of the numberpad keys is pressed, then the mouse moves to the centre of the targeted section and the preview window zooms in on that section, pressing another numberpad key refines the location until the desired target is under the cursor. At this point, you can press return to click. 

## Controls
* 1-9	Zoom window in on relevent section of the screen
* 0 	Reset zoom level
* +	Single Click
* <numberpad enter> Double Click
* -	Save location as first location for a drag (the next single click location initiates the drag

# TODO 
 - [x]  double click, 
 - [x]  drag, 
 - [ ]  Add a visual indicator (change colour of lines) when first drag point is taken. 
 - [ ]  Better mnemonics for click, doublce click extra, use the other hand
 - [ ]  Reset display after drag 
 - [ ]  Reset display switches off drag. 
 - [ ]  second click 
 - [ ]  Click in the preview window. 
 - [ ]  Keep the application selected
 - [ ]  Zoom out one level  
 - [x]  proper 3 by 3 overlay in the preview window
 - [x]  Improve speed - cache the screenshot for example. 
 - [ ]  settings from command line: always on top? preview window off? 
 - [ ]  The screen should indicate (colour of grid) if the program is active. 
 - [x]  Always on top
 - [ ]  Option to automatically focus on application window
 - [ ]  Hotkey to start
 - [x]  Applications need two clicks, but the top menu needs one click.... 
 - [ ]  put into stackexchange code review. 
 - [x]  refactor a whole lot.        
 - [x]  Fix the 'tile cannot extend outside image' bug.  
 - [ ]  It would be good if the screenshot periodically refreshed. 
 - [x]  On-mouse over would be nice. 
 - [x]  Screenshot should refresh whenever you tap to the system. 
 - [x]  Second set of minor grids to so that it's obvious what button you are going to press next 
 - [ ]  Do a profile to work out where the time is taken. 
 - [ ]  Would be occasionally nice to do a 2/3 zoom because the location I want is  on a boundary... (possibly with press and hold...) 
 - [ ]  Change the zones so that you don't zoom *completely* in a section is selected - so something on the boarder can be reached from both (The other approach is to have shortcuts to move the window to one side or other) 


# Statistics 
I'd like a statistics module - selfishly I'd like to know how many clicks I'm saving from WhatPulse, but I'd also like some general information like: 
 * how many numbers do I have to press to reach the correct location
 * How much time is taken per mouse click? 
 * Is it significantly faster when I do two number presses per refresh? 


