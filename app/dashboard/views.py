from flask import render_template
from flask_login import login_required
from app.dashboard import bp


@bp.route('/index')
@bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard/dashboard.html', title='Dashboard')
