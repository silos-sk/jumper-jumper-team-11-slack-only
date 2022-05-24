import random
from game.word import Word


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
      self._word = Word()
      self.guess = ""
      self.reveal = list(len(self._word._words)*'_')
      self.lives = 4
      self.won = False
      self.lose = False
      self.jumper ={
                    
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

      for i in range(0,len(self._word._words)):
          letter = self._word._words[i]
          if self.guess == letter:
              self.reveal[i] = self.guess
      if '_' not in self.reveal:
          return True
      else:
          return False


    def _glider(self):
      print(self.jumper[4 - self.lives])
      print(self.reveal)
      
    def process(self):
      while self.won == False and self.lives > 0:
          self._glider()
          self.guess = input('guess letter [a-z]: ')
          self.guess = self.guess.upper()
          
          if self.guess == self._word._words:
              self.won = True
              self.reveal = self._word._words
          if len(self.guess) == 1 and self.guess in self._word._words:
              self.won = self._check(self.guess, self._word._words)   
          else:
              self.lives-=1
          if self.won == True:
              print(f"nice! you guessed {self._word._words}")
              print("")
          else:
              print(" ")
          if self.lives == 0:
              self.lose = True
          if self.lose == True:
              print(self.jumper[4])
              print("You've lost")
              self.lost = False

