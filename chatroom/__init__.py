import os

from flask import Flask, render_template

from . import (Auth, Chat, Msg)
from . import db


def create_app(testing=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'chatroom.sqlite'),
    )
    print(app.config['DATABASE'])
     # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # if testing is None:
    #    app.config.from_pyfile('config.py', silent=True)
    # else:
    #    app.config.from_mapping(testing)
    app.register_blueprint(Auth.blueprint)
    app.register_blueprint(Chat.blueprint)
    app.register_blueprint(Msg.blueprint)

    print(app.url_map)

    # init the db
    db.init_app(app)

    return app


