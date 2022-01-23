import argparse
from pickle import NONE
import random
from wordfreq import word_frequency
from constants import *

def get_difficulty_to_words_map(difficulty=None):
    difficulty_to_words_map = {}
    for word in WORDS:
        difficulty = get_word_difficulty(word)
        if difficulty not in difficulty_to_words_map:
            difficulty_to_words_map[difficulty] = set(word)
        else:
            difficulty_to_words_map[difficulty].add(word)
    return difficulty_to_words_map if difficulty is None else difficulty_to_words_map[difficulty]

def get_word_difficulty(word):
    """
    Returns the difficulty of the word
    """
    frequency = word_frequency(word)
    if frequency >  0.0358:
        return 1
    elif frequency > 0.0179:
        return 2
    return 3

def get_word(length=None, difficulty=None):
    """
    Returns a random word from the dictionary of words
    """
    word_of_difficulty = get_difficulty_to_words_map(difficulty=difficulty)
    if length == 1:
        return random.choice(list(word_of_difficulty))
    
    word = NONE
    WORD_SEARCH_LIMIT = 1000
    for i in range(WORD_SEARCH_LIMIT):
        word = random.choice(list(word_of_difficulty))
        if len(word) != length:
            continue
    
    if word == NONE:
        raise Exception("Could'nt find a word of length {}, try again with a different length!".format(length))
    
    return word

def validate_args(args):
    print("Validating arguments...")
    if not args.word:
        args.word = get_word(args.length, args.difficulty)
    args.word = args.word.upper()
    if args.word not in WORDS:
        raise ValueError("Word not in dictionary")
    if args.difficulty not in DIFFICULTY_CHOICES:
        raise ValueError(
            "Difficulty must be one of {}".format(DIFFICULTY_CHOICES))
    if args.length < MAX_WORD_LENGTH or args.length > MAX_WORD_LENGTH:
        raise ValueError("Word length must be between {} and {}".format(
            MIN_WORD_LENGTH, MAX_WORD_LENGTH))
    if args.guesses < MAX_GUESSES or args.guesses > MAX_GUESSES:
        raise ValueError("Number of guesses must be between {} and {}".format(
            MIN_GUESSES, MAX_GUESSES))
    return args


def fetch_arguments_parser():
    parser = argparse.ArgumentParser(description='Worlde bot')
    parser.add_argument('-w', '--word', type=str,
                        help='Word to solve', default=None, required=False)
    parser.add_argument('-l', '--length', type=int,
                        help='Length of the word', default=None, required=False)
    parser.add_argument('-d', '--difficulty', type=str,
                        help='Difficulty of the word', default=None, required=False)
    parser.add_argument('--sol', '--solution', type=str,
                        help='Solution of the word', default=None, required=False)
    parser.add_argument('-g', '--guesses', type=str,
                        help='Number of gussess allowed', default=None, required=False)
    parser.add_argument('-s', '--slow', type=str, 
                        help='Wait for user input after every guess', default=None,
                        required=False)
    return parser
