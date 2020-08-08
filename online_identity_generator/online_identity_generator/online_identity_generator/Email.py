from .UserItem import UserItem

class Email(UserItem):
    def generate(self):
        from random import choice, randint
        from string import ascii_letters

        if self.topic.lower() == 'casual' or self.topic.lower == '':
            alphabet = list(ascii_letters)
            email1 = [f'{self.include_words}{randint(0,1000)}' for i in range(5)]
            return email1
