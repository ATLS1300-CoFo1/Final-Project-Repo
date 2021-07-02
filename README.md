# Final-Project-Repo
Start code and examples to get you to the finish line!

If the file has the word "func" in it, it is JUST a function. There is example code beneath that can be uncommented to see how it works, but you should be able to clean its function from looking the code.

**Boundary.py** is a module. Download it (green button), put it in the same folder as your script and import it with
`import boundary`
Example code is provided in the file.

**list_examples.py** shows 
1. how to make a list of turtles with a for loop
2. how to access the list using a for loop with i (indexing)
3. how to access the list using a for loop with turt (individual turtles)
4. how to access a list using modulo (indexing 2 different length lists in a for loop)

**There are two start code scripts available** 
OOP_Start.py describes how to set up using classes and object (like defining and calling functions)
Game_Start.py describes how to set up a procedural game. Has location for classes and objects, too.
_(You're gonna want to make sure you follow organization similar as to what's in here.)_

**Gallery viewer** is missing. Will provide later.

Email if you need more examples!

# Final Project Requirements
## All code must:
- be fully functional! Make sure you test your code by restarting your kernel and then running your code.
- meet all the requirements of your topic description (all rules met, the correct number of art pieces, keypresses, mouse clicks, etc.)
- be well commented! Label sections (classes, functions, tasks, etc.), write notes for any confusing or hard-to-follow sections, describe what functions do, etc.
- have any copied code MUST be cited (it's just good practice)
- have any bugs that persisted through your presentation should be commented and the fix described (ex. typo! needed to make a new variable, etc.)

## Make sure you should turn in:
1. your script (.py file)
2. any image files (.gif)
3. any new pseudocode since the milestone (if you get stuck, you should be writing pseudocode!)

I recommend working on your code in a new folder, and save all supplementary files in that folder. Then zip that folder and submit it. 
Zipping files: https://rasmussen.libanswers.com/faq/32413

# Requirements by Topic
## Game - OOP required
Make a complete game using Python and turtle. Complete means it has a start screen or button and a game over screen/text. You are not allowed to make the following games: snake, racing games, pong. Feel free to create your own game, or recreate a classic favorite! You may use outside code for inspiration/help, but can have no more than 20% borrowed code in your final project. For ideas, think of card games like War, Go Fish or how you can make a classic game blind friendly (sound-oriented). 

### Requirements:
1. At least 1 object from a class that you create!
  - You may use your MP button object but it must integrate with your game! That is the button must help your game play, not do something unrelated.
2.  Whether expanding or not, you must include at least 2 to your code:
  - good guys/bad guys (this is most easily done using objects) - some element of the game must increase or decrease difficulty (add/decrease time, speed up movements, remove points, freeze the game, etc.)
  - start screen - a full splash screen (Links to an external site.) that covers the entire screen. Ideally this describes the game and how to play (earn points/win). You may use a button to start or use click interaction on the panel.
  - end screen - a complete erasure of the game screen and a display of text (check out turtle.write()) or an end game image. You may add a retry/restart button if you like
  - restart game - at the end of the game, this button would reset the game to the beginning. This would have to update the while loop, and may or may not show the splash screen again
  - difficulty levels - in the start screen or BEFORE animation begins, you can have the selection of difficulty levels. This may do things like control the size of bubbles (smaller is harder), speed of the game, or amount of time, for example.
  - display current score during game - have a counter or score kept in a corner of the window of the game during game play
  - display final score/high score during the game - this is a tricky one to program. high score should keep the highest score despite when the game was played! This will require you to keep a file that stores the high score. Here is some example code for how to create such a file and open it. (You should be able to import the shelve library already.) https://stackoverflow.com/questions/16726354/saving-the-highscore-for-a-game

**Please clearly indicate the additions you are making using commenting in your code. Describe overarching/major changes in the description at the top of the code.**

 
## Digital Art Gallery - OOP Optional
Create a series of generative art pieces. The gallery should should draw from 3 pieces total, you can step through each piece with a click or key stroke (see Final Project example code). Each piece can be as simple or as complex as you like. To set up the gallery, you can have each image/animation show one after the other. Feel free to set music to it! This topic weighs heavily on creative and artistic values. Use of objects is strongly encouraged (read: this makes code excellent instead of good.)

1. Create 3 standalone .py files that, when run, create a generative art piece. This means there is a random element that changes some element of the piece each time. Each piece should lend to some overarching theme (seasons, moods, times of day, progression through a coding project...)
2. You must change at least 2 elements (position, size, speed, color, etc.) in each piece.
3. You should demonstrate smart development by using the same or similar functions in each script. What is the same across all of your pieces? You should probably turn that into a function (or better, an object!)
4. Name your scripts (.py files) with numbers so that the order of display can be discerened (ex. fallPalette1.py, springPalette2.py)
5. Submit all your image files with your code or you will lose points!!

**2pts extra credit** - Use an object to create an element in at least 2 of your scripts.

 
## Interactive Ad - OOP Required!
Create 1 ad that have some interaction (click or key press).  The ad should present a product or company. The interaction should explain the product or company--how it works, different flavors, etc. You may also try a quiz to select a product from a list of products for a potential consumer (segmenting).  You can make a spoof or link to an actual product. Website link tutorial available upon request.

1. Describe what the ad is based off of, or the goal of the ad in the description.
2. Describe (top of script) or display (use turtle to write text) instructions to the user. Assume the user is someone who does not know how to program, and is only going to interact with the final images.
3. You must have **at least 1 object** from a class that you create! A button is suitable, but should work seamlessly with your ad.
4. There should be some animation element (no click interaction). The animation can be a color changing background, the product moving around the screen, etc. It cannot happen in response to an interaction. The animated object should move with a function (i.e., call the animation function in the while loop to generate movement).
5. There should be at least 2 interactive elements. This can be multiple "screens" each with an interactive element, or multiple points of interaction (click, keypress, etc.).
6. The final ad should be a cohesive story, not just a random animation and interaction. Try to sell the product/company! Past submissions have included 1) a quiz or choose-your-own-adventure that allows the programmer to employ segmenting and offer the user a product based on their answers, 2) a display of a product or environment for the product, and the product displays when the user clicks. You can also think of having the user type in their name and display their name with the product, create a reset button (that counts as an interaction) so they can interact with your ad again.



