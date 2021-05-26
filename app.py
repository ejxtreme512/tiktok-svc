from tokify import trending
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/trending')
def get_trending():
    return jsonify(trending())

if __name__=='__main__':
    app.run(debug=False)