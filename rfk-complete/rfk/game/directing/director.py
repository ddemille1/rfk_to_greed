#new code
#from shared.point import Point
#from point import Point
#import pyray
from game.shared.point import Point
import random
from game.casting.artifact import Artifact
from game.casting.cast import Cast
from game.shared.color import Color
#end new 

CELL_SIZE = 30
FONT_SIZE = 30
COLS = 60
ROWS = 40
#BACKGROUND = pyray.load_texture('pictures\cethiel-desert-edit.png')

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service, audio_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._audio_service = audio_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        self._audio_service._start_audio_device()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
            self._audio_service._update_music()
            
        self._video_service.close_window()
        self._audio_service._close_audio_device()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)    

        #new code
        artifacts = cast.get_actors('artifacts')
        for artifact in artifacts:
            velocity = self._keyboard_service.move_down()
            artifact.set_velocity(velocity)
        # end new code    

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        score = cast.get_first_actor("scores")
        
        
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        #new code, this moves the artifacts
        artifacts = cast.get_actors('artifacts')
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
        #end new code  

        #This makes the artifacts disappear when the cursor hits them.
        point_value = 0
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                cast.remove_actor("artifacts", artifact)
                point_value = artifact.get_message() 
                score.sum_score(point_value)
            if artifact.get_position().get_y() == 0:
                cast.remove_actor("artifacts", artifact)
        #This checkes if # and each * or O are at the same position
        # if true, the point value of the * or O is assigned to a variable
        # this variable is used by the score object to sum the score
        # Then the score is obtained from the score object
        # finally the text of the score object is changed to display the score
        # everything is displayed by video service draw actors later in the game.     
        display_score = score.get_score()

        self._add_new_artifacts(cast)

        score.set_text(f"Score: {display_score}")

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        self._video_service.draw_background()
        actors = cast.get_all_actors()
        
        self._video_service.draw_actors(actors)
        
        self._video_service.flush_buffer()
        

    def _add_new_artifacts(self, cast):
        gain_point = 1
        lose_point = -1
        point_value = 0

        num_new_artifacts = random.randint(1,2)
        #this is looping through 40 times (number of default_artifacts)
        for n in range(num_new_artifacts):
            
            #this picks a random number, and gets the symbol associated with that number in unicode alphabet thingy. This is whats generating the random symbols for the artifacts.
            #this needs to be changed to just give x and o artifacts. 
            text = chr(random.choice([42, 79]))
            #this is assigning a message to each of the n artifacts
            if text == "*":
                point_value = gain_point
            elif text == "O":
                point_value = lose_point  

            #this is generating a random x position that will be used to put the artifacts
            #  in random places at the top of the screen
            x = random.randint(1, COLS - 1)
            y = 0
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            artifact.set_message(point_value)
            cast.add_actor("artifacts", artifact)

