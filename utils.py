import requests
import api_files as api

c_ID = api.client_id
c_secret = api.client_secret


def get_token(client_id, client_secret):
    response = requests.post('https://accounts.spotify.com/api/token', data={'grant_type': 'client_credentials'},
                             auth=(client_id, client_secret), verify=False)
    print(f'get_token:', response)
    access_token = response.json()['access_token']
    headers_auth = {'Authorization': 'Bearer ' + access_token}
    return access_token, headers_auth


def get_track_url(track_name):
    token, headers = get_token(client_id=c_ID, client_secret=c_secret)

    response = requests.get(f'https://api.spotify.com/v1/search?q=track:"{track_name}"&type=track', headers=headers,
                            verify=False)
    print(f'get_track:', response)
    return response.json()['tracks']['items'][0]['external_urls']['spotify']


def make_playlist():
    pass


def import_songs():
    pass
