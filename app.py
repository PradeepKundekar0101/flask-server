from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS from flask_cors

from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
CORS(app)  

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get-transcripts/<video_id>')
def get_transcripts(video_id):
    try:
        transcripts = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify(transcripts)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
