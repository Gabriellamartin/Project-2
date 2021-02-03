import spotipy
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from Config import Client_ID, Client_Secret
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
import json as json

data_path = "C://Users//BYoung//Documents//NU Bootcamp Files//Project 2//archive//data.csv"
data_artists = "C://Users//BYoung//Documents//NU Bootcamp Files//Project 2//archive//data_by_artist.csv"
data_genres = "C://Users//BYoung//Documents//NU Bootcamp Files//Project 2//archive//data_by_genres.csv"
data_year = "C://Users//BYoung//Documents//NU Bootcamp Files//Project 2//archive//data_by_year.csv"
data_artists_w_genre = "C://Users//BYoung//Documents//NU Bootcamp Files//Project 2//archive//data_w_genres.csv"
main_df = pd.read_csv(data_path)
genres_df = pd.read_csv(data_genres)
# yearly_df = pd.read_csv(data_year)
artist_df = pd.read_csv(data_artists_w_genre)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=Client_ID, client_secret=Client_Secret))


def song_info(song):
    # One API call to get all out information
    # May add an if statement to handle songs or artists
    track_results = spotify.search(q='track:' + song, type='track')
    track_items = track_results['tracks']['items'][0]
    # Parse the information for what we need
    track_artist_info = track_results['tracks']['items'][0]['artists'][0]
    track_imgs = track_results['tracks']['items'][0]['album']['images']
    track_popularity = track_results['tracks']['items'][0]['popularity']
    track_name = track_results['tracks']['items'][0]['name']
    track_preview = track_results['tracks']['items'][0]['preview_url']
    track_uri = track_results['tracks']['items'][0]['uri']
    release = track_results['tracks']['items'][0]['album']['release_date']

    release_convert = datetime.fromisoformat(release)
    release_date = str(release_convert.year)

    # Call to get the audio features for a song
    audio_features = spotify.audio_features(track_uri)

    # Call to get similar artists recommendaitons
    related_artists = spotify.artist_related_artists(track_artist_info['uri'])
    
    related_artists_list = []
    for name in related_artists['artists']:
        related_artists_list.append(name['name'])
    track_recommendations = []

    # yearly_df = pd.DataFrame(yearly_df)
    compare_df = pd.DataFrame(audio_features[0], index=[0])
    main_df['loudness'] = main_df['loudness'].abs()
    compare_df['loudness'] = compare_df['loudness'].abs()
    # yearly_df['loudness'] = yearly_df['loudness'].abs()

    compare_df['acousticness'] = compare_df['acousticness'][0] / main_df['acousticness'].max()
    compare_df['danceability'] = compare_df['danceability'][0] / main_df['danceability'].max()
    compare_df['energy'] = compare_df['energy'][0] / main_df['energy'].max()
    compare_df['instrumentalness'] = compare_df['instrumentalness'][0] / main_df['instrumentalness'].max()
    compare_df['liveness'] = compare_df['liveness'][0] / main_df['liveness'].max()
    compare_df['speechiness'] = compare_df['speechiness'][0] / main_df['speechiness'].max()
    compare_df['tempo'] = compare_df['tempo'][0] / main_df['tempo'].max()
    compare_df['valence'] = compare_df['valence'][0] / main_df['valence'].max()
    compare_df['loudness'] = compare_df['loudness'][0] / main_df['loudness'].max()

    main_df['acousticness'] = main_df['acousticness'] / main_df['acousticness'].max()
    main_df['danceability'] = main_df['danceability'] / main_df['danceability'].max()
    main_df['energy'] = main_df['energy'] / main_df['energy'].max()
    main_df['instrumentalness'] = main_df['instrumentalness'] / main_df['instrumentalness'].max()
    main_df['liveness'] = main_df['liveness'] / main_df['liveness'].max()
    main_df['speechiness'] = main_df['speechiness'] / main_df['speechiness'].max()
    main_df['tempo'] = main_df['tempo'] / main_df['tempo'].max()
    main_df['valence'] = main_df['valence'] / main_df['valence'].max()
    main_df['loudness'] = main_df['loudness'] / main_df['loudness'].max()

    yearly_avgs = main_df.groupby(['year']).agg({'acousticness': 'mean', 'danceability': 'mean', 'energy': 'mean', 'instrumentalness': 'mean', 'liveness': 'mean', 'loudness': 'mean', 'speechiness': 'mean', 'tempo': 'mean', 'valence': 'mean'})
    yearly_avgs = yearly_avgs.to_json(orient="columns")
    yearly_avgs = json.loads(yearly_avgs)
    year_attribute_keys = []
    year_attributes = []
    compare_keys = []
    compare_scale = []
    
    for i in compare_df.keys():
        compare_keys.append(i)
        for key, value in compare_df[i].items():
                compare_scale.append(value)
    

    for i in yearly_avgs.keys():
        year_attribute_keys.append(i)
        for key, value in yearly_avgs[i].items():
            if key == release_date:
                year_attributes.append(value)



    return({'Track_Title': track_name, 'Track_IMGS': track_imgs, 'Track_Popularity': track_popularity, 'Track_Preview_URL': track_preview, 'Related_Artists': related_artists_list, 
    'Audio_Features': audio_features, 'Track_Recommendatoins': track_recommendations, 'Release_Date': release_date, 'Compare_Keys': year_attribute_keys, 'Compare_Scale': compare_scale, 'Yearly_Avgs': year_attributes})

