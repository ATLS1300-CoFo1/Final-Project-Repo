#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:10:26 2021

@author: sazamore

This script will display your art by running your code, and then will allow
the user to step through the images using the left and right arrow keys.


Save this file in the same folder/repository as your individual scripts (.py).


When you run this code, a second window will pop up and show your art. To close that
window, simply hit the red X in the upper left corner. YOU MUST CLOSE THE
WINDOW BEFORE DISPLAYING THE NEXT PIECE. Ignore any white text errors that may
show up when running the code. It's all back-end gibberish that means very little.

Hit the red x on the GREEN MENU SCREEN to stop running the gallery.

YOU MUST END YOUR SCRIPT NAME WITH A NUMBER. (Ex. gallery1.py, gallery2.py)
"""
import turtle, glob, os


class GalleryManager(turtle.Turtle):
    def __init__(self):
        super().__init__() #inherit the screen (where we'll do the drawring)

        # get files
        self.fileList = [] # empty list for files
        for name in glob.glob("*.py"):
            if name[-4].isdigit():
                self.fileList.append(name) # get all files that end in numbers

        print("There are {} images in this gallery".format(len(self.fileList)))
        print("Use left and right arrows to step through them!")
        self.galIDX = 0 #gallery view index
        self.file = self.fileList[self.galIDX]
    
        self.menu = self.getscreen()
        self.ht()
        self.buildMenu()
                
        turtle.listen()
        # self.Screen.mainloop()
        turtle.done()
    def buildMenu(self):
        # set up screen size, position & title
        w = 700
        h = 200
        offset = 50
        self.menu.setup(width=w, height=h,startx=offset, starty=offset)
        self.menu.bgcolor("olivedrab1")
        self.menu.title("Generative Gallery Control Menu")
        
        # write instructions
        text = turtle.Turtle(visible=False)
        text.up()
        font = ("Helvetica",20,"bold")
        text.goto(-200,0)
        text.write("Use L and R arrows to display art!",
                   font=font)
        # hid all the turtles
        for turt in self.menu.turtles():
            turt.ht()

        #add keypress callbacks
        self.menu.onkey(self.incUp, "Right") # step through images to the right
        self.menu.onkey(self.incDown, "Left") # step through images to the left

    def displayArt(self):
        """runs the script based on list index"""
        self.file = self.fileList[self.galIDX]
        command = "python " + self.file
        os.system(command)

    def incUp(self):
        print("Drawing piece number {}".format(self.galIDX))
        print("This piece is titled '{}'".format(self.file[:-4]))

        # stop previous script
        command = "pkill " + self.file
        os.system(command)
        
        self.galIDX +=1
        if self.galIDX >= len(self.fileList):
            self.galIDX = 0
            
        self.displayArt()
        print(self.galIDX)
    
    def incDown(self):
        print("Drawing piece number {}".format(self.galIDX))
        print("This piece is titled '{}'".format(self.file[:-4]))
        # stop previous script
        command = "pkill " + self.file
        os.system(command)
        self.galIDX -=1
        if self.galIDX < 0:
            self.galIDX = len(self.fileList)-1
        self.displayArt()
        print(self.galIDX)

if __name__=="__main__":
    gal = GalleryManager()


# turtList = [] #empty list
# colors = ["red","green"] # "red" is colors[0], "green" is colors[1]
# numTriangle = 2

# for i in range(numTriangle): # range creates values 0, 1
#     turt = turtle.Turtle("triangle")
#     # customize turtle
#     turt.shapesize(2)
#     turt.color(colors[i])
#     # add turtle to turtList
#     turtList.append(turt)
    
# turtList[1].forward(50)