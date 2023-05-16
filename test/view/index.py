from flask import render_template, make_response
from test.test import view_bp
from test.test import STUDENTS


@view_bp.route("/", methods=['GET', 'POST'])
def index():
    response = make_response(render_template("index.html.j2", students=STUDENTS))
    response.set_cookie("test", "Devops_fantom")
    return response
    ## For Test:
    #return "hello-world"  
