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

        self.label = Label()

        return self.window


if __name__ == '__main__':
    app = MainApp()
    app.run()