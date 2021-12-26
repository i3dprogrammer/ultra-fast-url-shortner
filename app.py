import utils, db, os, config
from flask import Flask, request, render_template, url_for

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET'])
def add():
    url = request.args.get('url', None)
    code = request.args.get('code', None)
    if not url:
        return "Bad Request - There was no URL found to shorten.", 400
    else:
        if not code:
            code = utils.generate_random_code()
        # TODO: Add to databse.
        return render_template('index.html', original_url=url, shortened_code = code)

@app.route('/a/<string:code>', methods=['GET'])
def save_url(code):
    # TODO: Fetch code from database.
    return render_template('404.html', code=code)
