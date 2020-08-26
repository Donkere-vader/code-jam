from .UserItem import UserItem
from itertools import permutations

class Name(UserItem):
    def generate(self) -> list:
        """ The function you call to generate the names """
        self.names = []

        for keywords in permutations(self.parent.keywords, min(len(self.parent.keywords), 2)):
            self.names += self._generate(keywords)

        return self.names

    def _generate(self, keywoards) -> list:
        _names = []

        name = ""
        for k in keywoards:
            name += f"{k.capitalize()} "
        _names.append(name[:-1])

        return _names
