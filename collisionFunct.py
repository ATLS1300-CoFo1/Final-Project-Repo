"""
This is a function to detect collisions. A example of use is below. Uncommenting may not have the code run properly!
"""

def isCollision(turt,target,buffer=30):
    '''Detects collision with an object (turt) or list of objects (target).
    Made by Dr. Z
    Inputs:
      turt - the main object (MUST be a Turtle object)
      target - the collision target (can be Turtle object or list of Turtles object)
      buffer - area surrounding turt center that counts as a collision. Default value is 30 pixels. (int)
    Returns:
      Boolean value whether the two items have collided.'''
    
    target = target[:] # duplicate target
    x = turt.xcor() # get positions
    y = turt.ycor()
    
    if type(target)==list:
        # If it's a list, step through each value and check
        if turt in target: #is the turtle we're testing in the list we're colliding with?
            # makes sure the turtle doesn't collide with itself
            idx = target.index(turt) # find out where it is
            target.pop(idx) # remove it (just for the function)
            
        for i in range(len(target)):
            targX = target[i].xcor()
            targY = target[i].ycor()
            if round(targX)-buffer<=round(x)<=round(targX)+buffer and round(targY)-buffer<=round(y)<=round(targY)+buffer:
                return True
            else:
                return False
    elif type(target)== Turtle:
        # If it's a turtle, get its position and checks for collision
        targX = target[i].xcor()
        targY = target[i].ycor()
        if round(targX)-buffer<=round(x)<=round(targX)+buffer and round(targY)-buffer<=round(y)<=round(targY)+buffer:
            return True
        else:
            return False
    else:
        print("The argument that you've passed in as the main object is not a Turtle. Call the function again using a turtle. \n",
           "isCollision(Turtle())")
      
      
# =============================== EXAMPLE USE ==========================================
# import turtle
#
# create two turtles to test:
# turt1 = turtle.Turtle()
# turt2 = turtle.Turtle()
# turt3 = turtle.Turtle()
# turtList = [turt2, turt3] # this is not a pythonic way to make a list of turtles. Use a for loop.
#
# 
# create a variable to store the Boolean output of isCollision
# collided = isCollision(turt1,turtList) # checks to see if turt1 collided with either turt2 or turt3 (in list)
#
# use the output of isCollision() to perform actions based on whether a collision happened or not
# if collided:
#     print("A collision happened)
# else:
#     print("A collision did not happen")
