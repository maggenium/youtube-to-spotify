# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput

##
# Testing just the youtube api
##

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import os
import pprint # for prettier printing of dictionaries

def main():
    
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
        part="contentDetails",
        forUsername="MrSuicideSheep"
    )
    response = request.execute()

    # print('Type of response is: {}'.format(type(response)))
    # print('Keys: {}'.format(response.keys()), end='\n\n')
    # print('kind: {}'.format(response['kind']), end='\n\n')
    # print('etag: {}'.format(response['etag']), end='\n\n')
    # print('pageInfo: {}'.format(response['pageInfo']), end='\n\n')
    # print('items: {}'.format(response['items']), end='\n\n')

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

    # print video titles
    for i in range(len(playlist_items)):
        print('Video Nr. {}: {}'.format(i, playlist_items[i]['snippet']['title']))

    # pprint.pprint(first_video_title)

if __name__ == '__main__':
    main()