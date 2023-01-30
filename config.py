import os

basedir = os.path.abspath(os.path.dirname(__name__)) 

#path finds what file we're in
#being super specific... whatever __name__ is in, *that is the path that we want*

class Config():
    # FLASK_APP = 'run.py' #how do you get to your app
    # FLASK_ENV = 'development' #how to get to your env. by default it's "production".
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False