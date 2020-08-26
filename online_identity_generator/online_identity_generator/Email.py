from .UserItem import UserItem
from validate_email import validate_email  # to check if the email doesn't yet exist

class Email(UserItem):
    def generate(self):
        username = self.parent.username.get()
        usernames = self.parent.username.usernames
        usernames.remove(username)

        self.email = f"{username}@gmail.com"  # w'll only bother for gmail for now
        print(f"checking {self.email}")
        if validate_email(self.email, verify=True) is None:
            return self.email

        for username in usernames:
            self.email = f"{username}@gmail.com"  # w'll only bother for gmail for now
            print(f"checking {self.email}")
            if validate_email(self.email, verify=True) is None:
                return self.email
