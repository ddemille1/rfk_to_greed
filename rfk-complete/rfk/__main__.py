import os
import random
import raylib
from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point



FRAME_RATE = 15
MAX_X = 1800
<<<<<<< HEAD
MAX_Y = 720
=======
MAX_Y = 900
>>>>>>> 578003249c681932ec55a1f08fe7820e8b2673fa
CELL_SIZE = 30
FONT_SIZE = 30
COLS = 60
ROWS = 40
CAPTION = "Greed"
#DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 80


def main():
    
    # create the cast
    cast = Cast()
    
    
    # create the score
    score = Score()
    score.set_text("")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("scores", score)


    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - CELL_SIZE)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts

    #this is getting the data file of random messages, reading it line by line, spliting it up, and returing each line as the message that's displayed when the robot hits the artifact.

    # gain_point = 1
    # lose_point = -1
    # point_value = 0

        
  


    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()