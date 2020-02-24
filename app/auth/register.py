from flask import request, session, redirect, url_for, flash, render_template

from .resources import auth
from .models import User, db, Account


@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        try:
            assert request.form['username'] is not None, 'Username is required'
            assert request.form['password'] is not None, 'Password is required'
            assert request.form['first_name'] is not None, 'First Name is required'
            assert request.form['last_name'] is not None, 'Last Name is required'

            existing_user = User.query.filter_by(username=request.form['username']).first()
            assert existing_user is None, 'User {} is already registered.'.format(request.form['username'])

            u: User = User(
                username=request.form['username'],
                account_id=0,
                first_name=request.form['first_name'],
                last_name=request.form['last_name']
            )
            u.set_password(request.form['password'])
            db.session.add(u)
            db.session.commit()

            return redirect(url_for('auth.login'))

        except AssertionError as e:
            flash(e)

    return render_template('auth/register.jinja2')