from game.terminal_service import TerminalService
from game.parachute import Parachute
from game.word import words


"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/jumper-specification.html
"""


class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self.parachute = Parachute()
        self.word = words
    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Update this comment
        Args:
            self (Director): An instance of Director.
        """
        self.word

    def _do_updates(self):
        """Update this comment
        Args:
            self (Director): An instance of Director.
        """
        self.parachute._process()

    def _do_outputs(self):
        """Update this comment
        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service
        pass
