from flask_restplus import Namespace, Resource, fields
# from ..core import run_spiders
from json import dumps
from flask import jsonify
import json
from ..models import Student
from ..schemas import student_schema,students_schema
from flask import request
api = Namespace('students', description='students')


@api.route('/',methods=['GET','POST'])
class Student_API(Resource):
    def get(self):
        # contact2 = Student('nduhio', 'male', '123', 'uthiru', 'cheche@gmail.com', '20', 'python')
        contact1 = Student('obama', 'male', '001', 'kinoo', 'obama@gmail.com', '20', 'java')
        # contact1.save()
        students=Student.get_all()
        # contact2.save()
        # json_students = []

        # for item in students:
        #     json_students.append(student_schema.jsonify(students[0]))
        # print(len(students))
        results = students_schema.jsonify(students)
        return results
    
    # def post(self):
    #     api
    #     # json_data = request.get_json()
    #     print (api)

@api.route("/new", methods=["POST"])
class add_user(Resource):
    def post(self):
        username = request.json
        
        # new_user = User(username, email)

        # db.session.add(new_user)
        # db.session.commit()
        return jsonify(username)
 
    # def post(self):
    #     new_student = Student()

# print("the code runs")

# @api.route('/week/<number>',methods=['GET','POST'])
# class Scraped_fixtures(Resource):
#     def get(self,number):
#         matches=Match.get_week(number)
#         results = {'week': matches}
#         return jsonify(results)