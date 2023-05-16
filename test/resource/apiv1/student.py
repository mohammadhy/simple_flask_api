from flask import request
from flask_restful import Resource
from test.test import STUDENTS

class StudentResource(Resource):
    def get(self):
        return "GET"
        #return {"students": STUDENTS}

    def post(self):
        data = request.get_json()
        student = {
                   "name": data.get("name"),
                   "family": data.get("family")
                  }
        STUDENTS.append(student)
        return { "students" : student }

