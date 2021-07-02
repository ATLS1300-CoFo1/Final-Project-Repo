"""
Simple coundtown timer using turtle. This timer is set to countdown from 30, updates once a second. Prints text on screen.
Modified from: https://www.codetoday.co.uk/post/creating-a-simple-timer-in-python-and-using-it-with-programs-in-turtle

Now compatible with while loops. 

YOU MUST IMPORT THE TIME LIBRARY FOR THIS TO WORK

"""
def timer_start():
  """Creates a turtle and timer. Use in conjunction with timerUpdate().
  Call the line above a while loop!"""
  global timer_text, start
  timer_text = turtle.Turtle()
  start = time.time()
  
def timerUpdate(duration):
    """updates a timer.
    Inputs:
        duration - time in seconds that the game should last (int)
    Returns:
        a boolean. False if below the time limit, True if above."""
    global run, running, start, timer_text
    
    timer_text.clear() # this will ONLY clear the timer
    timer_text.write(int(time.time() - start), font=("Courier", 30)) # write the time left on the screen, whole seconds only
  
    return time.time() - start > duration
        
    
    
#=======================  EXAMPLE OF USE ====================================
# import time
# THE TIME LIBRARY IS REQUIRED FOR THIS TO WORK
#
# duration = 30 # length of game, in seconds
# running = True
# timer_start()
# 
# while running:
#      timeOut = timerUpdate(duration)
#
#      if timeOut:
#          print("Time's up!")
#      else:
#          print("Keep going!")

