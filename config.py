import os
basedir = os.path.abspath(os.path.dirname(__file__))
# from dotenv import load_dotenv

# # load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dummy password'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False