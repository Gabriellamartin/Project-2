from flask import Flask, render_template, url_for, jsonify, request
import pprint
import spoticall
from spoticall import song_info

app = Flask(__name__)

song = []
api = []


@app.route('/')
def testing():
    return render_template('index.html')

@app.route('/2021-2025 Predictions')
def testing():
    return render_template('index.html', embed=Kalebsjavascript)


@app.route('/songinteraction', methods=['GET', 'POST'])
def access_song():
    global song
    global api
    if request.method == 'POST':
        song = request.form['song_input']
        api = song_info(song)


    return render_template('index.html', embed=api)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5002)