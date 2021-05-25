from tokify import trending
from flask import Flask

app = Flask(__name__)


@app.route('/trending')
def get_trending():
    return trending()

if __name__=='__main__':
    app.run(debug=False)