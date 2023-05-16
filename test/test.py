from flask import Flask, Blueprint
from flask_restful import Api

STUDENTS = []

view_bp = Blueprint("view", __name__)
#
apiv1_bp = Blueprint("apiv1_bp", __name__ ,url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

print(apiv1)

from test import view
from test import resource



def create_app():
    app = Flask(__name__)
    app.register_blueprint(view_bp)
    app.register_blueprint(apiv1_bp)
    return app


