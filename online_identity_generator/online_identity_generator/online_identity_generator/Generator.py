from .Username import Username
from .Password import Password
from .Email import Email
from .Name import Name
from .ProfilePicture import ProfilePicture



class User:
    def __init__(self, keywords):
        self.keyword = keywords
        self.username_class = Username(self)
        self.name_class = Name(self)
        self.password_class = Password(self)
        self.email_class = Email(self)
        self.profile_picture_class = ProfilePicture(self)

    def generate(self):
        self.name = self.name_class.generate()
        self.usernames = self.username_class.generate()
        self.passwords = self.password_class.generate()
        self.email = self.email_class.generate()
        self.profile_picture = self.profile_picture_class.generate()
        
        
        
#Input Script
if __name__ == '__main__':
    help_input = input("Type 'help' for more info on how our program works, otherwise click 'Enter': ")
    if help_input.lower() == 'help':
        print('''
        
        #TODO write something over here, I'm too lazy atm =p
        
        ''')

    include_words = input('*What word do you want to be included in your username?: ')
    topic = input('For what are you going to use this username for (gaming, social-media, business, casual)?: ')
    spec_char = input('Do you want any special characters included in your name( "-", "_", ".")?: ')
    x = Username(spec_char,include_words, topic)

    print(f'This was the topic you chose: "{x.topic}" ')
    print(f'This was the word we included in your username: "{x.include_words}" ')

    #Display-Name Script
    print(f'These are the names we generated for you =): {x.generate_name()}')

    #UserName Script
    print(f'These are the usernames we generated for you =): {x.generate_username()}')

    #Email Script
    print(f'This is the email we generated for you =): {x.generate_email()}')
