import os
import random
import hashlib
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
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    headers = {
        'Authorization': PEXELS_API_KEY,
    }
    params = {
        'query': text,
        'per_page': 10 
    }
    response = requests.get('https://api.pexels.com/videos/search', headers=headers, params=params)
    videos = response.json().get('videos', [])

    if not videos:
        return jsonify({'videoUrl': None})

    random.shuffle(videos) 
    selected_video = videos[0]
    video_url = selected_video['video_files'][0]['link']

    hash_object = hashlib.md5(text.encode())
    video_filename = f'output_{hash_object.hexdigest()}.mp4'

    video_response = requests.get(video_url)
    with open(video_filename, 'wb') as f:
        f.write(video_response.content)

    return jsonify({'videoUrl': f'/{video_filename}'})

@app.route('/<filename>')
def output_video(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
