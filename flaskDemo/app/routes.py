from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # return 'Hello World!'
    user = {'username':'duke'}
    return render_template('index.html',title='首页',user=user)