from flask import url_for
from flask import request
from flask import redirect
from flask import render_template

from app import db
from app import app
from models import Lake
from models import River
from models import Country
from models import Language


@app.route('/')
@app.route('/lakes')
def lakes():
    lakes = Lake.query.all()
    return render_template('lakes.html', lakes=lakes)


@app.route('/rivers')
def rivers():
    rivers = River.query.all()
    return render_template('rivers.html', rivers=rivers)
