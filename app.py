import youtube_dl
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# return the audio url of the video
def returnAudioUrl(url):
    with youtube_dl.YoutubeDL({'format': 'bestaudio/best'}) as ydl:
        result = ydl.extract_info(url,download=False)
        return (result.get('url'))

# search youtube using youtube-dl and return the audio url of first result
def search(query):
    with youtube_dl.YoutubeDL({'format': 'bestaudio/best'}) as ydl:
        playlist = ydl.extract_info(f'ytsearch:{query}',download=False)
        return (playlist.get('entries')[0].get('url'))

# redirect to the audio url of the video
@app.route('/')
def redirect_url():
    if request.args.get('url'):
        try:
            url = request.args.get('url')
            return redirect(returnAudioUrl(url))
        except Exception as e:
            return jsonify({"error": str(e)})
    elif request.args.get('query'):
        try:
            query = request.args.get('query')
            return redirect(search(query))
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "Please enter the video url. Doc: https://github.com/matumasadev02/youtube-dl-audio-api/blob/master/README.md"})

# return the audio url of the video
@app.route('/info')
def return_url():
    if request.args.get('url'):
        try:
            url = request.args.get('url')
            return jsonify({"url": returnAudioUrl(url)})
        except Exception as e:
            return jsonify({"error": str(e)})
    elif request.args.get('query'):
        try:
            query = request.args.get('query')
            return jsonify({"url": search(query)})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "Please enter the video url. Doc: https://github.com/matumasadev02/youtube-dl-audio-api/blob/master/README.md"})

if __name__ == '__main__':
    app.run()