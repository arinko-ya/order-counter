from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app.auth.models import User
from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm, PasswordChangeForm


@bp.route('/index')
@bp.route('/')
def index():
    user = {'username': 'momopanda'}
    return render_template('auth/index.html', title='Home', user=user)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('menu.menu'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', category='danger')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('menu.menu'))
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.index'))


@login_required
@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(name=form.username.data).first():
            flash(f'[{form.username.data}] is already exist.',
                  category='danger')
            return redirect(url_for('auth.register'))
        else:
            User.create(form.username.data, form.password.data)
            flash('Registration completed')
            return redirect(url_for('auth.register'))
    return render_template('auth/register.html', title='Register', form=form)


@login_required
@bp.route('/password_change', methods=['GET', 'POST'])
def password_change():
    form = PasswordChangeForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        if not user.check_password(form.current_password.data):
            flash('Current password is incorrect', category='danger')
            return redirect(url_for('order.password_change'))
        user.password_change(form.new_password.data)
        flash('Password changed')
        logout_user()
        return redirect(url_for('auth.login'))
    return render_template('auth/password_change.html',
                           title='Password Change', form=form)
