import os
from flask import Flask, request, jsonify, send_file, render_template
import requests

app = Flask(__name__)

PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.json
    text = data.get('text')

    headers = {
        'Authorization': PEXELS_API_KEY,
    }
    params = {
        'query': text,
        'per_page': 1
    }
    response = requests.get('https://api.pexels.com/videos/search', headers=headers, params=params)
    videos = response.json().get('videos', [])

    if not videos:
        return jsonify({'videoUrl': None})

    video_url = videos[0]['video_files'][0]['link']
    video_response = requests.get(video_url)
    video_path = 'output.mp4'
    with open(video_path, 'wb') as f:
        f.write(video_response.content)

    return jsonify({'videoUrl': '/output.mp4'})

@app.route('/output.mp4')
def output_video():
    return send_file('output.mp4', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
