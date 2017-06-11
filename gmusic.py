from gmusicapi import Mobileclient
from conf import user
from conf import password

api = Mobileclient()
api.login(user, password, Mobileclient.FROM_MAC_ADDRESS)

#playlists = api.get_all_playlists(incremental=False, include_deleted=None)
#playlist_id = [playlist['id'] for playlist in playlists if playlist['name'] == 'Test playlist']
playlist_id = api.create_playlist('test playlist2')
#print playlist_id
library = api.search('Gorillaz Revolving door', max_results=1)
song = library['song_hits'][0]['track']
#print song
storeid = song['storeId']
nid = song['nid']
api.add_songs_to_playlist(playlist_id, storeid)
#api.get_all_user_playlist_contents


