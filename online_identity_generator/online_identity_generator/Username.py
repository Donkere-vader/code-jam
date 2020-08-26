from random import random, choice
from .UserItem import UserItem
from itertools import permutations

class Username(UserItem):
    def generate(self) -> list:
        """ The function you call to generate the usernames """
        self.usernames = []

        print(f"Keywords: {self.parent.keywords}")

        for keywords in permutations(self.parent.keywords, min(len(self.parent.keywords), 3)):
            self.usernames += self._generate(keywords)

        return self.usernames

    def _generate(self, keywords) -> list:
        """ Generate a couple of usernames on a specific set of keywoards (with taking the order into a count) (and the keywords used here can be a subset of the total keywoards)"""
        _usernames = []

        username = ""
        for k in keywords:
            username += f"{k}_"
        _usernames.append(username[:-1])

        username = ""
        for k in keywords:
            username += k.capitalize()
        _usernames.append(username)

        return _usernames
