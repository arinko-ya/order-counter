from flask import Blueprint

bp = Blueprint('order_counter', __name__)

from app.order_counter import routes