from .UserItem import UserItem
from google_images_search import GoogleImagesSearch

class ProfilePicture(UserItem):
    self.gis = GoogleImagesSearch('your_api_key', 'your_project_cx')

    def generate(self):
        _search_params = {
            'q': self.parent.name.get(),
            'num': 10,
            'safe': 'high|medium|off',
            'fileType': 'jpg|gif|png',
            'imgType': 'clipart|face|lineart|news|photo',
            'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
            'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow',
            'usageRights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
        }

        result = self.gis.search(search_params=_search_params, path_to_dir='../static/tmp/pfp/', width=500, height=500)

        print(result)
