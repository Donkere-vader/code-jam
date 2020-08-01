from .UserItem import UserItem

class Username(UserItem):
    def generate(self):
        from random import choice, randint
        from string import ascii_letters

        if self.topic.lower() == 'casual' or self.topic.lower == '':
            alphabet = list(ascii_letters)
            usernames1 = [f'{self.include_words}{randint(0,1000)}' for i in range(5)]
            usernames2 = [f'{self.include_words}{self.spec_char}{choice(alphabet)}{choice(alphabet)}' for i in range(5)]
            return usernames1, usernames2