#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:37:35 2020

@author: Dr. Z
@author: YOUR NAME

DELETE this line for full credit - this script, as-is, blinks a turtle on blue backgnd to show framerate

***DESCRIPTION: What does your game do? What is the goal? How do you know when you win or lose?***
"""


import random, turtle

#=============================GLOBAL VARIABLES============================

#==============================CLASSES================================

class changeTHisName(turtle.Turtle):
    pass # delete this and replace with your code.

#==========================DEFINE FUNCTIONS=============================
def setup(w=600,h=600,tracer=False, origin="center"):
    """Sets up screen and settings for ATLS1300 most likely uses. Has 2 optional arguments:
        w - (int) screen width, in pixels, default is 600
        h - (int) screen height, in pixels, default is 600
        tracer - (Bool) if True, turns off animation, if False keeps Turtle animation.
        origin - (str) use "upperleft" to put origin in upper left
    makes panel a global variable for use throughout code."""
    global panel
    #Create a panel to draw on. 
    turtle.setup()
    panel = turtle.Screen()
    panel.clear()
    w = 600 # width of panel
    h = 600 # height of panel
    panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
    turtle.colormode(255)
    if tracer:
        turtle.tracer(0)
        print("don't forget to use panel.update() to draw your art!")
    if origin=="upperleft":
        panel.setworldcoordinates(0, w, h, 0)
        

#===============INITIAL CONDITIONS==================
setup()

# Define your start variables here!
frameInterval = 100 # The time, in ms, between frames. Increase value to slow animation, decrease value to speed up animaton
run = True

# make objects here, make lists here

#=======================GAME LOOP (Execution)=========================

while run:
    # call animation function
    
    # run check function(s) that control gameover or end of user experience
   
    
    turtle.delay(frameInterval) #set frame rate
    panel.update() # update the image with each "frame"

panel.mainloop() # keep listeners on for mouse press
turtle.done()
        