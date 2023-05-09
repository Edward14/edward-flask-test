from flask import Flask
from app.route import hello_world, index

def create_app():
    # app = Flask(__name__)
    app = Flask(__name__, template_folder='templates') 
    app.add_url_rule('/', '/', hello_world)
    app.add_url_rule('/index', 'templates/index', index)
    return app