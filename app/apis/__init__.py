from flask_restplus import Api
from flask import Blueprint

apis = Blueprint('api', __name__)

api = Api(apis, version='1.0', title='Sports API',
    description='sports fixtures, standings and livescore API',
)

from .teams import api as teams

api.add_namespace(teams)
