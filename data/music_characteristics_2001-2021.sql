SELECT * FROM spotify_data
WHERE spotify_data.year > 2000;

SELECT spotify_data.acousticness, spotify_data.danceability, spotify_data.energy, 
spotify_data.instrumentalness, spotify_data.liveness, spotify_data.loudness, 
spotify_data.speechiness, spotify_data.valence, spotify_data.year, spotify_data.artists
FROM spotify_data
WHERE spotify_data.year > 2000
ORDER BY spotify_data.year ASC;