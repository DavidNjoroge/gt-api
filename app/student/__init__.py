from flask_restplus import Api
from flask import Blueprint

apis = Blueprint('student', __name__)

api = Api(apis, version='1.0', title='Students',
    description='storing students data API',
)

from .views import api as views

api.add_namespace(views)
