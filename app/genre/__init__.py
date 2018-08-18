from flask import Blueprint

bp = Blueprint('genre', __name__)

from app.genre import views