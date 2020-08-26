from .Username import Username
from .Password import Password
from .Email import Email
from .Name import Name
# from .ProfilePicture import ProfilePicture

class User:
    is_active = True  # to use flask login

    def __init__(self, keywords, id):
        self.id = id
        self.keywords = keywords
        self.username = Username(self)
        self.name = Name(self)
        self.passwords = Password(self)
        self.email = Email(self)
        # self.profile_picture = ProfilePicture(self)

    def get_id(self):
        return self.id
