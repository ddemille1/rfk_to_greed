import os
import random
import raylib
import pyray
from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.audio_service import AudioService

from game.shared.color import Color
from game.shared.point import Point



FRAME_RATE = 20
MAX_X = 800
MAX_Y = 450
CELL_SIZE = 30
FONT_SIZE = 30
COLS = 60
ROWS = 40
CAPTION = "Greed"
MUSIC_PATH = os.path.dirname(os.path.abspath(__file__)) + "/resources/cycle_music_game.wav"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 80
BACKGROUND_PATH = os.path.dirname(os.path.abspath(__file__)) + "/resources/background.png"



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
    video_service = VideoService(BACKGROUND_PATH, CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    audio_service = AudioService(MUSIC_PATH)
    director = Director(keyboard_service, video_service, audio_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()