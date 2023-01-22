# Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.

import os
import re

class File_stats:
    def __init__(self, file = ""):
        self.lines = 0
        self.words = 0
        self.characters = 0
        self.sentences = 0
        self.file = file
        self.__count_stats()
    
    def __count_stats(self):
        infile = open(self.file, 'r')
        for line in infile:
            line = line.strip(os.linesep)
            self.sentences = self.sentences + len(re.findall(r'[.?!]+', line))
            wordslist = line.split()
            self.lines = self.lines + 1
            self.words = self.words + len(wordslist)
            self.characters = self.characters + len(line)

    def get_stats(self):
        print("Filename:", self.file)
        print("Lines:", self.lines)
        print("Words:", self.words)
        print("Characters:", self.characters)
        print("Sentences:", self.sentences)

    def recount_stats(self):
        self.__count_stats()

baby_shark = File_stats("lab124.txt")

baby_shark.get_stats()
