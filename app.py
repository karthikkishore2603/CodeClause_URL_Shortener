from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import constants

app.config["SQLALCHEMY_DATABASE_URI"] = constants.SQLALCHEMY_DATABASE_URL
app.config["SECRET_KEY"] = constants.FLASK_SECRET_KEY
db = SQLAlchemy(app)

import crud,models
@app.get('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST','GET'])
def index_post():
    data = dict(request.form)
    original_url = data['original_url']
    short_url = data['short_url']

    crud.add_url(data)        
    return render_template('index.html',original_url=original_url,short_url=short_url)


@app.route('/<short_url>')
def redirect_to_url(short_url):
    datas = crud.search(short_url)
    ourl = datas.original_url
    surl = datas.short_url
    print(ourl)
    
    if 'https://' in ourl:
        red = ourl
    elif 'http://' in ourl:
        red = ourl
    else:
        red = 'https://'+ourl

    if short_url == surl:
        return redirect(red)
    else:
        return '404 Not Found'

