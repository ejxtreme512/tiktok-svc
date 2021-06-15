from flask import Flask, jsonify
from flask.helpers import send_file
from flask_cors import CORS
from tokify import user_by_username, tiktok_by_id, tiktoks_by_user, tiktoks_by_trending, video_by_id

app = Flask(__name__)
CORS(app)


@app.route('/tiktoks/trending')
def get_trending():
    return jsonify(tiktoks_by_trending())


@app.route('/tiktoks/<user>')
def get_trending(user):
    return jsonify(tiktoks_by_user(user))


@app.route('/users/<<user>')
def get_user_by_username(user):
    return user_by_username(user)


@app.route('/download/<id>')
def get_video_by_id(id):
    return send_file(video_by_id(id), attachment_filename="tiktok_" + id + ".mp4", as_attachment=True, mimetype='video/mp4')


@app.route('/info/<id>')
def get_tiktok_by_id(id):
    return jsonify(tiktok_by_id(id))


if __name__ == '__main__':
    app.run(debug=False)
