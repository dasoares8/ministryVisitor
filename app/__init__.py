# To simplify locating the application, add the following import statement
#from .flaskr import create_app
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('EVM_SETTINGS', silent=True)
    app.debug = app.config['DEBUG']
    return app

app = create_app()
import eucharisticVisitManager.views