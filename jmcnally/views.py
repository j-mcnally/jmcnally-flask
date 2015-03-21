from flask import render_template
from jmcnally import app 

@app.route('/')
def index():
    return render_template('index.html.haml')
