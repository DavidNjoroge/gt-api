
from . import ma


class StudentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name','gender','reg_no','address', 'email','age','language')
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


# 'david', 'male', '123', 'uthiru', 'njoroge@gmail.com', '20', 'python'