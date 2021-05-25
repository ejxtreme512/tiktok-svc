from tokify import get_trending
from flask import Flask


app = Flask(__name__)


@app.route('/trending')
def trending():
    return get_trending()

if __name__=='__main__':
    app.run()