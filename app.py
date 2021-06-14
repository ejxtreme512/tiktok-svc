from flask import Flask, jsonify
from flask.helpers import send_file
from flask_cors import CORS
from tokify import tiktok_by_id, tiktoks_by_user, trending, video_by_id

app = Flask(__name__)
CORS(app)


@app.route('/trending')
def get_trending():
    return jsonify(trending())


@app.route('/username/<user>')
def get_tiktok_by_user(user):
    return jsonify(tiktoks_by_user(user))


@app.route('/download/<id>')
def get_video_by_id(id):
    return send_file(video_by_id(id), attachment_filename="tiktok_" + id + ".mp4", as_attachment=True, mimetype='video/mp4')


@app.route('/info/<id>')
def get_tiktok_by_id(id):
    return jsonify(tiktok_by_id(id))


if __name__ == '__main__':
    app.run(debug=False)
