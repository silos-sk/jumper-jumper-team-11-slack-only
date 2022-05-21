import random
from game.word import words


class Parachute:
    

    def __init__(self):
      self.word = words
      self.guess = ""
      self.reveal = list(len(self.word)*'_')
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
    
    
    
  def check(self, letter, word):
      """Checks the word to see is the letter guessed is in the word."""

      for i in range(0,len(self.word)):
          letter = self.word[i]
          if self.guess == letter:
              self.reveal[i] = self.guess
      if '_' not in self.reveal:
          return True
      else:
          return False


    def glider(self):
      print(self.jumper[4 - self.lives])
      print(self.reveal)
      
    def _process(self):
      while self.won == False and self.lives > 0:
          self.glider()
          self.guess = input('guess letter [a-z]: ')
          self.guess = self.guess.upper()
          
          if self.guess == self.word:
              self.won = True
              self.reaveal = self.word
          if len(self.guess) == 1 and self.guess in self.word:
              self.won = self.check(self.guess, self.word)   
          else:
              self.lives-=1
          if self.won == True:
              print(f"nice! you guessed {self.word}")
              print("")
          else:
              print(" ")
          if self.lives == 0:
              self.lose = True
          if self.lose == True:
              print(self.jumper[4])
              print("You've lost")
              self.lost = False
              print(self.word)

