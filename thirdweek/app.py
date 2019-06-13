#!/usr/bin/env python3

from flask import Flask
from flask import url_for
from flask import redirect
from flask import request
from flask import make_response
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)

@app.route('/user/<username>')
def user_index(username):
    resp = make_response(render_template('user_index.html',username=username))
    resp.set_cookie('username',username)
    return resp

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('user_index',username='shixiaolou'))
    print(url_for('show_post',post_id=1,_external=True))
    print(url_for('show_post',post_id=2,q='python 03'))
    print(url_for('show_post',post_id=2,q='python can'))
    print(url_for('show_post',post_id=2,_anchor='a'))
    return 'test'

@app.route('/<username>')
def hello(username):
    if username == 'shixiaolou':
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
    print('method:',request.method)
    print('name:',request.form.get('name'))
    print('password:',request.form.get('password'))
    print('hobbies:',request.form.getlist('hobbies'))
    print('age:',request.form.get('age',default=18))
    return 'registered successfully!'

if __name__ == '__main__':
    app.run()
