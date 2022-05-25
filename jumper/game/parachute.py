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
      '''
         Responsibility:
         To construct a new Parachute.

         Args:
         self (Parachute): an instance of Parachute.
      '''  

      self._word = Word().words() 
      self.guess = ""
      self.reveal = list(len(self._word)*'_')
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
      '''
         Responsibility:
         To track the guess and the letter in the word.

         Args:
         self (Parachute): an instance of Parachute.
         letter (string): the guessed letter.
         word (string): the random word to be guessed.
      '''

      for i in range(0, len(word)):
          letter = word[i]
          if self.guess == letter:
              self.reveal[i] = self.guess
      if '_' not in self.reveal:
          return True
      else:
          return False


    def _glider(self):
      '''
         Responsibility:
         To cut off a line from the parachute and show the correct guessed letters. 

         Args:
         self (Parachute): an instance of Parachute.
      '''

      print(self.jumper[4 - self.lives])
      print(self.reveal)
      
    def process(self):
      '''
         Responsibility:
         To
         
         Args:
         self (Parachute): an instance of Parachute.
      '''

      while self.won == False and self.lives > 0:
          self._glider()
          self.guess = input('guess letter [a-z]: ')
          self.guess = self.guess.upper()
          
          if self.guess == self._word:
              self.won = True
              self.reveal = self._word
          if len(self.guess) == 1 and self.guess in self._word:
              self.won = self._check(self.guess, self._word)   
          else:
              self.lives-=1
          if self.won == True:
              print(f"nice! you guessed {self._word}")
              print("")
          else:
              print(" ")
          if self.lives == 0:
              self.lose = True
          if self.lose == True:
              print(self.jumper[4])
              print("You've lost")
              self.lost = False

