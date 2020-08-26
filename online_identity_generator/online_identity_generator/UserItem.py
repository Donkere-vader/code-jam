class UserItem:
    def __init__(self, parent):
        self.parent = parent

    def get(self):
        """ Get the selected value """
        return self.selected_item

    def sel(self, val):
        """ Selected the chosen item """
        self.selected_item = val
