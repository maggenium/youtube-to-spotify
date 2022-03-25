from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import os

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


class MainApp(App):
    def build(self):

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        dev_key = "AIzaSyBdEhVKgYQ83fnLC2cZ54Ct7Fbv1U20s1c"

        # Create API client
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=dev_key)

        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            forUsername="MrSuicideSheep"
        )
        response = request.execute()

        # fetch uploads playlist id
        content_details = response['items'][0]['contentDetails']
        uploads_playlist_id = content_details['relatedPlaylists']['uploads']

        # fetch uploads playlistItems
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=20
        )
        response = request.execute()
        
        playlist_items = response['items']
        video_titles = []
        # print video titles
        for i in range(len(playlist_items)):
            video_titles.append(str(playlist_items[i]['snippet']['title']) + '\n')

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        label_str = '\n'.join(video_titles)
        self.label = Label(text=label_str,
                           font_size=18,
                           color='orange'
        )
        self.window.add_widget(self.label)

        return self.window


if __name__ == '__main__':
    app = MainApp()
    app.run()