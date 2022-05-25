# Invoke the random module.
import random

class Word:
    '''
       Responsibility:
       To have a list of words and select a random word from the list.

       Attributes:
       _word_list (List[string]): A list of words to select from.
    '''

    def __init__(self):
        '''
           Responsibility:
           To construct a new Word.

           Args:
           self (Word): an instance of word.
        '''

        self._word_list = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", 
          "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing","buzzwords", 
          "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", 
          "embezzle", "equip", "espionage", "euouae","exodus", 
          "faking", "fishhook", "fixable", "fjord", "flapjack",
          "gabby", "galaxy", "galvanize", "gazebo","giaour", 
          "haiku", "haphazard", "hyphen", 
          "iatrogenic", "icebox", 
          "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", 
          "kayak", "kazoo", "keyhole", "khaki", "kilobyte",
          "larynx", "lengths", "lucky", "luxury", "lymph", 
          "marquis", "matrix", "megahertz", "microwave", "mnemonic", 
          "naphtha", "nightclub","nowadays", "numbskull", "nymph", 
          "onyx", "ovary", "oxidize", "oxygen", 
          "pajama", "phlegm","pixel", "pizazz", 
          "quartz", "queue", "quips", "quixotic", "quiz", 
          "rhubarb", "rhythm", "rickshaw", 
          "schnapps", "scratch", "shiv", "snazzy", "sphinx", 
          "thriftless", "thumbscrew", "topaz", "transcript", "transgress", 
          "unknown", "unworthy", "unzip", "uptown", 
          "vaporize", "vixen", "vodka", "voodoo", "vortex", 
          "walkway", "waltz", "wave", "wavy", "wyvern", 
          "xylophone", 
          "yachtsman", "yippee", "yoked", "youthful", "yummy", 
          "zephyr", "zigzag", "zigzagging", "zilch", "zombie"]


    def words(self):
        '''
           Responsibility:
           To select a random word from the list.

           Args:
           self (Word): an instance of Word.

           Returns:
           string: The random word selected.
        '''

        random_word = random.choice(self._word_list).upper()
        return random_word