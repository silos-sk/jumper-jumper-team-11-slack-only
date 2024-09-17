import random
class Word:
 def __init__(self):
  """
      Responsibility:
       Selects a random words from a list of words.
       Attributes:
         display_list (List[string]): A list of words to select from.
         _words (str): Random word selected from the list.
  """
  self._words = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom",
"azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle",
"bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing",
"buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri",
"dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae",
"exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "gabby", "galaxy", "galvanize", "gazebo",
"giaour", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "jackpot", "jaundice", "jawbreaker",
"jaywalk", "jazziest", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "larynx", "lengths", "lucky",
"luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "naphtha", "nightclub",
"nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "phlegm",
"pixel", "pizazz", "quartz", "queue", "quips", "quixotic", "quiz", "rhubarb", "rhythm",
"rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "thriftless", "thumbscrew", "topaz",
"transcript", "transgress", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka",
"voodoo", "vortex", "walkway", "waltz", "wave", "wavy", "wyvern", "xylophone", "yachtsman", "yippee", "yoked",
"youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zombie"] 
 def get_words(self): 
  display_list = random.choice(self._words).upper()
  return display_list
