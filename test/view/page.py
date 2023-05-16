from flask import request
from test.test import view_bp

@view_bp.route("/page")
def page():
    return request.cookies.get("test")

