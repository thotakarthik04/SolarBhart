# this file will make this webpage folder a python package
from flask import Flask

# create flask app
def create_app():
    app=Flask(__name__)
    # configure flask app to encrypt cookies and session data
    app.config['SECRET_KEY']='@root'
    
    from .calc import calc
    app.register_blueprint(calc)    
    return app