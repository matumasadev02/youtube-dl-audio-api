import youtube_dl
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

def returnAudioUrl(url):
    with youtube_dl.YoutubeDL({'format': 'bestaudio/best'}) as ydl:
        result = ydl.extract_info(url,download=False)
        return (result.get('url'))

@app.route('/get')
def return_url():
    try:
        url = request.args.get('url')
        return jsonify({"url": returnAudioUrl(url)})
    except Exception as e:
        return jsonify({"error": str(e)})
@app.route('/')
def redirect_url():
    try:
        url = request.args.get('url')
        return redirect(returnAudioUrl(url))
    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == '__main__':
    app.run()