"""Word Finder: finds random words from a dictionary."""
from random import choice as choice

class WordFinder:
    def __init__(self, relative_path):
        # Source: Opening a txt file (6/29/2021): https://realpython.com/working-with-files-in-python/
        word_list = open(relative_path)
        # Source: prepping data from file to be used (6/29/2021): Exercise Solution
        self.words = self.read_file(word_list)
        # Source: (6/29/2021): Exercise Solution
        print(f"{len(self.words)} words read")
    
    def find_word(self, search_word):
        if search_word in self.words:
            return f"{search_word} is on line {self.words.index(search_word)} of words list"
        else:
            return f"{search_word} not found"
    
    # Source: prepping data from file to be used (6/29/2021): Exercise Solution
    def read_file(self, word_list):
        parsed_words = []
        for word in word_list:
            # Source: Understanding strip() (6/29/2021): https://www.programiz.com/python-programming/methods/string/strip
            parsed_words.append(word.strip())
        return parsed_words


    def random(self):
        # Source: Understanding choice() (6/29/2021): https://www.geeksforgeeks.org/python-numbers-choice-function/
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    def read_file(self, word_list):
        parsed_words = []
        for word in word_list:
            # Source: (6/29/2021): Exercise Solution
            if not word.strip().startswith("#"):
                parsed_words.append(word.strip())
        return parsed_words