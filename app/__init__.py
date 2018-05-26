from flask_restplus import Api
from flask import Blueprint
# from .teams import api as teams
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask import Flask
from flask_marshmallow import Marshmallow

db=SQLAlchemy()
ma = Marshmallow()

def create_app(config_name):
    app=Flask(__name__)

    #creatimg the app configurations
    app.config.from_object(config_options[config_name])

    #intializing flask extensions
    # bootstrap.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    # registering the blueprints

    from .student import apis as student_blueprint
    app.register_blueprint(student_blueprint)

    from .apis import apis as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .spiders import spiders as spiders_blueprint
    # app.register_blueprint(spiders_blueprint)

    # setting config
    # from .request import configure_request
    # configure_request(app)
    return app



# blueprint = Blueprint('api', __name__)
# api = Api(blueprint)
#
# api = Api(
#     title='My Title',
#     version='1.0',
#     description='A description',
#     # All API metadatas
# )
#
# api.add_namespace(teams)
