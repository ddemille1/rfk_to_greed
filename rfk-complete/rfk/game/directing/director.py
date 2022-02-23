#new code
#from shared.point import Point
#from point import Point
from game.shared.point import Point
#end new 

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

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
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                cast.remove_actor("artifacts", artifact)
            
        point_value = 0
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                point_value = artifact.get_message() 
                score.sum_score(point_value)
        display_score = score.get_score()
        
        score.set_text(f"Score: {display_score}")

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    # def _score_output(self):
    #     """This is goint to contain the code for tracking the score """
    #     score = 0
    #     banner = cast.get_first_actor("banners")
    #     banner.set_text(f"Score: {score}")
