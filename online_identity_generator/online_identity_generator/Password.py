from .UserItem import UserItem
from string import ascii_letters, punctuation
from random import choice

class Password(UserItem):
    password_length = 15

    def generate(self):
        self.chars = []
        self.chars += list(ascii_letters)
        self.chars += list(punctuation.replace("'", "").replace('"', '').replace("`", ""))
        self.chars += [str(i) for i in range(10)]

        self.passwords = []

        for i in range(10):  # generate 10 passwords
            self.passwords.append(self._generate())

        return self.passwords

    def _generate(self):
        password = ""

        for i in range(self.password_length):
            password += choice(self.chars)

        return password
