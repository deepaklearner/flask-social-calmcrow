from flask import Flask
from config import Config

app = Flask(__name__)

from app import routes
app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
        # debug=True,
        # use_reloader=True)
    