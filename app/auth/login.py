from flask import request, session, redirect, url_for, flash, render_template

from .resources import auth
from ..auth.models import User


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        try:
            assert request.form['username'] is not None, 'Username is required'
            assert request.form['password'] is not None, 'Password is required'
            u: User = User.query.filter_by(username=request.form['username']).first()
            assert u is not None, 'Incorrect username.'
            assert u.check_password(request.form['password']), 'Incorrect password.'

            session.clear()
            session['user_id'] = u.id
            return redirect(url_for('auth.index'))
        except AssertionError as e:
            flash(e)

    return render_template('auth/login.jinja2')
