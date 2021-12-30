# Scramble Console App: Details about the Application and Database created using Python, PostgreSQL, and more.

**Author: Jadesola Alade-Fa**

Developed over a series of months and adivised with the help of several instructors of the Nucamp bootcamp for Back End, SQL, and DevOps. Scramble was established to enhance familiarity with technologies and languages used in the creation and management of Python web applications and relational databases. The task of the project was to create an application that is solely based in-terminal, without the aid of a GUI.  

---

## Introduction  

**The Application**  

“Scramble!” is a spelling game that gives players random letters that they can use to spell words 
and earn points. The game offers two different levels of gameplay: novice and advanced. The novice 
level offers lower point earning potential, but more turns. The advanced level offers higher point 
earning potential, but less turns. Arrow key operated menus are utilized by the player for movement 
across different windows in-game, and an entry box setup to capture player input during gameplay. The 
main windows accessible to the player include: the starting menu window, the instructions windows, 
the level-select window, leaderboard, the game window, and the game-over window. The player can only exit or play 
the game through option selection in the starting menu.

**The Backend**  

Player scores are captured and stored into a PostgreSQL database. The game is simple so it was determined that three tables was sufficient. 

The tables belong to a PostgreSQL database include:    
* __levels__ - a table that holds the level names programmed into application (NOVICE and ADVANCED at the moment)

* __difficulties__ - a table that holds the application's programmed game difficulties; Associated attributes per difficulty is represented as field names: id, turn_count, multiplier, and level_id.

* __runs__  - a table holding randomly generated data where each record represents a player's: run-through id, name, score, level id, and difficulty id.  



I chose to use the SQL Alchemy ORM to develop my project's backend. I made the decision because I wanted to challenge myself and learn something unfamiliar. I think picking up new technologies quickly is a valuable skill and I don't mind the practice. I learned just enough that I was able to create a minimal, but functioning back-end for my application. 

---


**Thanks & Credits**  
To my loyal and loving testers – my family.

---  

**References**  
  
answerSeeker, --. (2017, August 13). How to make text fit inside a python curses textbox? Stack 
Overflow. Retrieved October 12, 2021, from https://stackoverflow.com/questions/45656335/how-tomake-text-fit-inside-a-python-curses-textbox. 
  
Bijay Kumar and Bijay KumarEntrepreneur. 2021. How to create countdown timer using python tkinter 
(step by step). (September 2021). Retrieved September 24, 2021 from 
https://pythonguides.com/create-countdown-timer-using-python-tkinter/
  
Chrisldema. (2020, December 13). Arrow Keys not read by python in integrated terminal. cursor doesn't 
turn off. · issue #112405 · Microsoft/VSCODE. GitHub. Retrieved October 12, 2021, from 
https://github.com/microsoft/vscode/issues/112405. 
  
Eva. (2020, October 30). How to make a countdown timer in Python (+bonus pomodoro tutorial!) | 
intermediate python project. YouTube. Retrieved October 12, 2021, from 
https://www.youtube.com/watch?v=ZPFXZmzvodA. 
  
Frank Cleary. 2014. Data science bytes. (November 2014). Retrieved September 24, 2021 from 
https://www.datasciencebytes.com/bytes/2014/11/03/get-a-list-of-all-english-words-in-python/
  
Kim, E., & et al. (2019, July 2). Pylint no member issue but code still works vscode. Stack Overflow. 
Retrieved October 12, 2021, from https://stackoverflow.com/questions/56844378/pylint-no-memberissue-but-code-still-works-vscode. 
  
Kuchling, A. M., & Raymond, E. S. (n.d.). Curses programming with python¶. Curses Programming with 
Python - Python 3.10.0 documentation. Retrieved October 16, 2021, from 
https://docs.python.org/3/howto/curses.html. 
  
Refsnes Data. (n.d.). Python Random choices() Method. Python random choices() method. Retrieved 
October 12, 2021, from https://www.w3schools.com/python/ref_random_choices.asp. 
  
serhiy-storchaka, birkenfeld, ezio-melotti, & et al. (2007). Curses - terminal handling for character-cell 
displays¶. curses - Terminal handling for character-cell displays - Python 3.10.0 documentation. 
Retrieved October 12, 2021, from https://docs.python.org/3/library/curses.html. 
  
Singh, N. K. (2019, March 27). Creating menu display for terminal | intro to curses in Python (part-2). 
YouTube. Retrieved October 12, 2021, from https://www.youtube.com/watch?v=zwMsmBsC1GM.
