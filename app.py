import youtube_dl
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

def returnAudioUrl(url):
    with youtube_dl.YoutubeDL({'format': 'bestaudio/best'}) as ydl:
        result = ydl.extract_info(url,download=False)
        return (result.get('url'))

@app.route('/')
def redirect_url():
    if request.args.get('url') != "":
        try:
            url = request.args.get('url')
            return redirect(returnAudioUrl(url))
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "please enter the video url."})
@app.route('/get')
def return_url():
    if request.args.get('url') != "":
        try:
            url = request.args.get('url')
            return jsonify({"url": returnAudioUrl(url)})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "Please enter the video url. Doc: https://github.com/matumasadev02/youtube-dl-audio-api/blob/master/README.md"})
if __name__ == '__main__':
    app.run()