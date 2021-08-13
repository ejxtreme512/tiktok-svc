from sql import add_user_favorites_list, add_user_to_users, get_favorite_list_items_by_list_id, get_favorites_list_by_user_id
from flask import Flask, jsonify
from flask.helpers import send_file
from flask import request
from flask_cors import CORS
from tokify import user_by_username, tiktok_by_id, tiktoks_by_user, tiktoks_by_trending, video_by_id

app = Flask(__name__)
CORS(app)


@app.route('/download/<id>')
def get_video_by_id(id):
    return send_file(video_by_id(id), attachment_filename="tiktok_" + id + ".mp4", as_attachment=True, mimetype='video/mp4')


@app.route('/favorites/user', methods=['POST'])
def add_user():
    email = request.form.get('email')
    last_name = request.form.get('last_name')
    first_name = request.form.get('first_name')
    return add_user_to_users(email, last_name, first_name)


@app.route('/favorites/user/<id>', methods=['GET'])
def get_user_favorites_list(id):
    return get_favorites_list_by_user_id(id)


@app.route('/favorites/list', methods=['POST'])
def add_favorite_list():
    user_id = request.form.get('user_id')
    list_name = request.form.get('list_name')
    add_user_favorites_list(user_id, list_name)


@app.route('/favorites/list/<id>', methods=['GET'])
def get_favorites_list(id):
    return get_favorite_list_items_by_list_id(id)


@app.route('/info/<id>')
def get_tiktok_by_id(id):
    return jsonify(tiktok_by_id(id))


@app.route('/tiktoks/trending')
def get_trending():
    count = int(request.args.get('count'))
    print('TRENDING', count)
    return jsonify(tiktoks_by_trending(count))


@app.route('/tiktoks/<user>')
def get_tiktoks_by_user(user):
    return jsonify(tiktoks_by_user(user))


@app.route('/users/<user>')
def get_user_by_username(user):
    return user_by_username(user)


if __name__ == '__main__':
    app.run(debug=False)
