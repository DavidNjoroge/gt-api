from flask import Blueprint

spiders = Blueprint('api', __name__)

from . import matches_spider
