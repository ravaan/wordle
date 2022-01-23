MIN_GUESSES = 3
MIN_WORD_LENGTH = 3
DEFAULT_WORD_LENGTH = 5
DEFAULT_NUM_GUESSES = 6
DIFFICULTY_CHOICES = [1,2,3]
DEFAULT_DIFFICULTY = 2
MAX_GUESSES = 10
MAX_WORD_LENGTH = 10
FILENAME = "./words.txt"
def load_dict(filename=FILENAME):
    """
    Loads the dictionary of words from the file words.txt
    """
    with open(filename, "r") as f:
        words = f.read().splitlines()
    return words
WORDS = load_dict(FILENAME)