from .UserItem import UserItem

class Name(UserItem):
    def generate(self):
        from random import choice, randint
        from string import ascii_letters

        if self.topic.lower() == 'casual' or self.topic.lower == '':
            alphabet = list(ascii_letters)
            name1 = [f'{self.include_words}{randint(0,1000)}' for i in range(5)]
            name2 = [f'{self.include_words}{self.spec_char}{choice(alphabet)}{choice(alphabet)}' for i in range(5)]
            return name1, name2
