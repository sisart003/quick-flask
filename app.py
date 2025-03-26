from flask import Flask, url_for, request, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"


# @app.route('/<name>')
# def hello(name):
#     return f"Hello, {escape(name)}!"


# Variable Rules
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     # X:\user\flask-tutorial\app
#     return f'Subpath {escape(subpath)}'


# # Unique URLs / Redicretion Behavior
# @app.route('/projects/')
# def projects():
#     return 'The project page'

# URL Building
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('projects'))
#     print(url_for('projects', next='/'))
#     print(url_for('show_user_profile', username='John Doe'))
    
    
# HTTP Methods
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'POST'
#     else:
#         return 'GET'
    

# Rendering Templates
# @app.route('/world/')
# @app.route('/world/<name>')
# def world(name=None):
#     return render_template('base.html', person=name)


# # Context Locals
# with app.test_request_context('/world', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block such as basic assertions:
#     assert request.path == '/world'
#     assert request.method == 'POST'
    
    
# Request Object
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'], request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method was GET or the credentials were invalid
#     return render_template('login.html', error=error)