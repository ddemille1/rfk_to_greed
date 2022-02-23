from game.casting.actor import Actor

class Score(Actor):
    """This is an actor that keeps track of the score of the game."""

    def __init__(self):
        self._score = 0
        super().__init__()

    def get_score(self):
        """gets the score classe's score
        
        Returns: (int) the score """ 

        return self._score

    def sum_score(self, points):
        """This adds the score as the game progresses
        
        Args: points (int): the points that are to be added to the score"""
        self._score += points   
        