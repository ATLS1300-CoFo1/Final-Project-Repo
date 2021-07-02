#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:55:44 2021

@author: sazamore

WORKING WITH LISTS - EXAMPLES
"""
import turtle

# Create a list of turtles

numElements = 3 # number of elements you want in your list
yourList = [] # empty list

# using a for loop to make a list
for i in range(numElements):
    # in this for loop, i has the values of 0 through (numElements-1) use it for indexing!
    
    turt = turtle.Turtle() # create a model turtle to add to your list
    turt.shapesize(20) #change the size or whatever you want to do to your turtle
    turt.up() # pick up the pen of every turtle
    
    yourList.append(turt) # add your turtle to the list
    
# ============= THERE ARE 2 WAYS TO ACCESS LISTS USING FOR LOOPS =============
# using a for loop to access a list
for turt in yourList:
    # in this for loop, turt has each turtle in the list, one after the other
    
    # this works well when you need to move or perform a function on every item
    # in a list, but NOT multiple lists!
    turt.forward(100)
    

# using a for loop to access multiple lists
colorList = ["red", "orange", "azure"]

for i in range(len(yourList)):
    print(yourList[i])
    print(colorList[i])
    
    #f I want to change the colors of every turtle in the list:
    yourList[i].color(colorList[i])
  # yourList[i] accesses the list of turtles
  # colorList[i] accesses the list of colors
        
        
       
# ============= BONUS: MODULOOOOOOOOOOOO =============

# using modulo to have continuous use of values despite differences in list length
yourList.append(turtle.Turtle()) # now the lists have different lengths

print("yourList is {} elements long.".format(len(yourList)))
print("colorList is {} elements long.".format(len(yourList)))

# use the for loop with modulo! 
for i in range(len(yourList)): 
    #step through the shorter list
    print("color before: "+yourList[i].color()[0])
    
    # print(i&len(colorList)) #uncomment to learn the ancient ways of Modulo
    
    yourList[i].color( colorList[ i % len(colorList) ] ) #access one list, modulo the length of the other list
   
    # the modulo indexing formula is: i % len(shorterList)
    print("color after: "+yourList[i].color()[0])
      
