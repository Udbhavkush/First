from flask import Flask, render_template
from flask_compress import Compress
from flask_restful import Api

app = Flask(__name__, static_folder='templates/static')
Compress(app)
api = Api(app)
app.secret_key = 'secret_key'

@app.route('/')
def index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8000, debug=True)