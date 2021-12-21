# RejuvVoltorbFlipper
A program designed to play Voltorb Flip in Pokemon Rejuvenation - please read the README.txt before trying to use the program.


This program is designed specifically for Pokemon Rejuvenation Version 13.0.5 and has not been tested on any other versions of this game or similar games.
This program is designed specifically for my machine and has not been tested on any other devices.

Right; In theory this program should work for anyone with a 1920 x 1080 monitor/screen resolution while playing the game in large screen size with "Turbo Speed" enabled and set to 4x. To fit this to any other sizing or resolutions, you will need to edit values on lines: 48 - 69, 80 - 85, 90 - 103, 167 - 169 and 432; Everything else should be fine. Commenting is sparse however I have left a comment above all the most important function, but I apologise if you want to delve deeper into it, it may not be clear what I have done and some functions may even be redundant from earlier versions.

There are 3 versions of the code in current form:
SetTheStage5.0.py - This will play a single game of Voltorb Flip to completion automatically. If you would like it to just show you the next move instead of playing it itself, simply set the variable 'play' to = False at the top of the file.
AutoPlayer1.0.py - This will play as many games as it can until it crashes with an output into the console showing you the programme's thought process and decision making, there is no hotkey to stop the programme running, however, minimising Rejuvenation should cause an error and force stop it looping.
FLIPPERTRON_300.py - My ultimate creation! The Flipper to beat all Flippers! Its literally just AutoPlayer1.0 without any outputs! oh...

In order to actually run the code, go to the Voltorb Flip table in the Crisola Hotel or in GDC leisure hall left hand room. Make sure the red outline is on the top left most tile and click play! The game screen must be in its original position and unimpeded as the programme screen scrapes. It also moves the mouse and uses the arrow keys as well as the space bar for transparency (set the variable 'play' to False at the top of the file if you don't want this to happen). I wrote and ran the code in PyCharm on Python Version 3.8.

There are prior versions of the code in folder labeled 'OldVersions' (crazy, I know), these should mostly work but bug fixes have only been done on the versions not in this folder.

You need to download the Board_Data folder to the same place as the Python flies so they can read them, Levels 1-4 come free, just need unzipping, Levels 5+ are with the paid DLC... just kidding, the board data for Levels 5 and beyond is beyond 25MB AFTER compressing, and thats per level, so uh, its big. And I can't upload them easily here. 
