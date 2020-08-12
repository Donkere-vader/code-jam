 # imports should be at the top of the file
from random import choice, randint
from string import ascii_letters
from .UserItem import UserItem

class Username(UserItem):

    def __init__(self, parent, usernames, topic, alphabet, include_words):

        super().__init__(parent, usernames, topic, alphabet, include_words)

        self.parent = parent
        self.usernames = usernames
        self.topic = topic
        self.alphabet = alphabet
        self.include_words = include_words

        
        
        # using a list in stead of two seperate varibles is cleaner code
        self.usernames = []
      
        # adding all the other variables to this class   
 
    def generate(self):
        if self.topic.lower() == 'casual' or self.topic.lower == '':
            alphabet = list(ascii_letters)

            # just use the one username list
            self.usernames += [f'{self.include_words}{randint(0,1000)}' for i in range(5)]
            self.usernames += [f'{self.include_words}{self.spec_char}{choice(alphabet)}{choice(alphabet)}' for i in range(5)]
            return usernames
