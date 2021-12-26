import utils, os
from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

from models import urls

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
        url_model = urls(code, url)
        db.session.add(url_model)
        db.session.commit()
        return render_template('index.html', original_url=url, shortened_code = code)

@app.route('/a/<string:code>', methods=['GET'])
def save_url(code):
    # TODO: Fetch code from database.
    url_model = urls.query.filter_by(code=code).first()
    if url_model:
        return url_model.url, 200
    return render_template('404.html', code=code)
