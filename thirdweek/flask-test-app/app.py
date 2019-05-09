#!/usr/bin/env python3

from flask import Flask,render_template,abort

app = Flask(__name__)

@app.route('/user/<username>')
def user_index(username):
    if username == 'invalid':
        abort(404)
    return render_template('user_index.html',username=username)
