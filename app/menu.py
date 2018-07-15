from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('menu', __name__)


@bp.route('/')
@login_required
def menu():
    return render_template('menu.html', title='Menu')
