from flask import Flask, jsonify
from flask.helpers import send_file
from tokify import trending, video_by_id

app = Flask(__name__)


@app.route('/trending')
def get_trending():
    return jsonify(trending())


@app.route('/download/<id>')
def get_video_by_id(id):
    return send_file(video_by_id(id), attachment_filename="tiktok_" + id + ".mp4", as_attachment=True, mimetype='video/mp4')


if __name__ == '__main__':
    app.run(debug=False)
