import random
from game.word import Word
from game.terminal_service import TerminalService


class Parachute:
    """The parachute image determining the limit of the game. 
    The responsibility of a Parachute is to display the image of the parachute and reduces its gliders if the user makes an erroneous guess
    Attributes:
        word: the generated random word from the set word list
        guess: a letter guessed by the user
        reveal: reveal correctly guessed letter
        lives: total user lives
        won: user has won
        lose: user has lost
        jumper: parachute image states
        
    """

    def __init__(self):
      self.word = Word().get_words()
      self.terminal_service = TerminalService()
      self._guess = ""
      self._reveal = list(len(self.word)*'_')
      self._lives = 4
      self._won = False
      self._lose = False
      self._jumper ={
                    
0: """
            ___  
           /___\ 
           \   / 
            \ /               
             0   
            /|\  
            / \  
          
           ^^^^^^^""",

1:"""                 
           /___\ 
           \   / 
            \ /  
             0   
            /|\  
            / \  
                    
           ^^^^^^^""",
                   
2:"""          
           \   / 
            \ /  
             0   
            /|\  
            / \  
          ^^^^^^^""",

3:"""          
            \ /  
             0   
            /|\  
            / \  
          ^^^^^^^""",

4:"""
             x   
            /|\  
            / \  
          
          ^^^^^^^"""}
    
    
    
    def _check(self, letter, word):
      """ 
      Function that returns true or false if the parachute is present or not.
      Args:
      self(_reveal): An instance of Parachute.
      """

      for i in range(0,len(self.word)):
          letter = self.word[i]
          if self._guess == letter:
              self._reveal[i] = self._guess
      if '_' not in self._reveal:
          return True
      else:
          return False


    def _glider(self):
      """Function that creates the parachute and updates it.
      Args:
        Print the parachute form.
      """
      print(self._jumper[4 - self._lives])
      print(self._reveal)
      
    def process(self):
      """
      Function that checks if the guess letter is in the word and returns true or false if the guess is correct or not.
      Args:
      An instance of parachute.
      guess: Boolean to maintain parachute
      """
      while self._won == False and self._lives > 0:
          self._glider()
          self._guess = input('guess letter [a-z]: ')
          self._guess = self._guess.upper()
          
          if self._guess == self.word:
              self._won = True
              self._reveal = self.word
          if len(self._guess) == 1 and self._guess in self.word:
              self._won = self._check(self._guess, self.word)   
          else:
              self._lives-=1
          if self._won == True:
              self.terminal_service.write_text(f"You have found the correct word! Congratulations! Game over {self.word}")
              self.terminal_service.write_text("")
          else:
              self.terminal_service.write_text(" ")
          if self._lives == 0:
              self._lose = True
          if self._lose == True:
              self.terminal_service.write_text(self._jumper[4])
              self.terminal_service.write_text("You didn't guess the word! Game over.")
              self.lost = False
