from flask import Flask, render_template, url_for, jsonify, request
import pprint
import spoticall

app = Flask(__name__)

song = []


@app.route('/')
def testing():
    return 'Hello'


@app.route('/songinteraction', methods=['GET', 'POST'])
def access_song():
    global song
    if request.method == 'POST':
        song = request.form['song_input']
    # return jsonify(song)

    # return ('index.html', embed=song)
    return render_template('index.html', embed=song)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
