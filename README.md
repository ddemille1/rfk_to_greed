
## Greed##

**Greed** 
Greed is a game in which the player seeks to gather as many falling gems as possible. Gather a gem(*) and get a point. Gather a rock(o) and you lose a point. Keep playing until your greed is satisfied.

---
## Getting Started

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 rfk 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the rfk-complete/rkf folder and click the "run" icon.



## Project Structure
The project files and folders are organized as follows:
```
root                        (project root folder)
+-- Game                    (source code for game)
  +--Casting           
    +-- object.py           (code for object class)
    +-- point.py            (code for point class)
    +-- cast.py             (code for cast class)
    +-- score.py             (code for score class)
  +--Directing          
    +--director.py          (code for director class)
  +--Services
    +--keyboard_service.py  (code for keyoard_service class)
    +--video_service.py     (code for video_service class)
  +--Shared
    +--color.py             (code for color class)
    +--point.py             (code for point class)
  +-- __main__.py           (program entry point)
+-- README.md               (general info)
``` 

## Required Technologies
* Python 3.8.0
* Raylib 3.7

## Authors
Jonathan Trok, Douglas DeMille, McKenna Wall, Ruth Ale Bravo 
group: bartholomew_nathanael