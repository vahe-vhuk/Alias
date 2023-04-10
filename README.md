# Alias
INTRODUCTION The digital version of the well-known board game, made using Python's library PyQT5. The programme consists of several files. All the programming is carried out using Python3 and the Python library PYQT5

ABOUT THE APPLICATION A Graphically generated application allows the user to see the game Alias on a new window, which pops up after they run the code. First, appears  six buttons: "Play", "Rules", "Add word", "Gamemode", "Gamerule" and "Language". After the user clicks on either of them the whole layout changes based on what they have clicked. Each layout change is a new page. Add word allows the user to add words whatever they want to the base of words, which will be discussed later. Originally there are more than 700 English 900 Russian and 1100 Armenian words, which are mainly nouns. After writing the word, by simply clicking Add button the system automatically adds the word to the base if possible. After which the user will receive a message about the status of the word being added. After pressing the Gamemode button, the user is asked to choose the number and names of teams, that are going to play the game. After pressing the Gamemode button,  the user is asked to choose Round duration with seconds and the Win-score. And After pressing the "Play" button, the game is ready to start.

TECHNOLOGIES The project is carried out using Python3.11 and Python library PyQT5. https://doc.qt.io/qtforpython/ The core of the programme is the Class MainWindow which inherits its main features from QMainWindow and each of pages inherits its main features from QLabel. UI is sliced between several classes. Which is the reason for it being too short and readable. In UI the main thing that helps to organize the page-changing the effect is carried out using OOAD, which allows us to have simple code for the each of pages. the InGame words are generated randomly which is carried out using the choise module from Random

GAME RULES Alias is a team game.
On the "Game Mode" page we can add or reduce  the number of playing groups (2-4 groups).
On the "Settings" page, you can select the duration of one round (20-180 seconds), 
as well as  the number of points required to win the game (20-400 units).
On the "Add word" page you can addwords that are not listed in the recommended words.
(The words must contain only Armenian letters)
During the game, for every guessed word the team gets one point, 
if the some of the given words are not guessed and the player presses "Next", 
the team loses a point for every unguessed word.
The playing team does not lose points if all of the sugested 5 words are not guessed or 
if the time is up.

THE PROJECTS AIM The project is done for educational purposes.

BEFORE LAUNCH Before Launch please make sure you have all the necessities, which include the following: -Python (at least 3.11 version) https://www.python.org/downloads/ -PyQt 5 library https://pypi.org/project/PyQt5/

HOW TO LOUNCH If you have all the requirements, in the command line go to the game directory, and press ''python3 main.py"
