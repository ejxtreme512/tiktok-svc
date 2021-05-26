from tokify import trending, video_by_id
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/trending')
def get_trending():
    return jsonify(trending())


@app.route('/download/<id>')
def get_video_by_id(id):
    return video_by_id(id)
if __name__=='__main__':
    app.run(debug=False)