from flask import Blueprint, abort, flash, render_template
from flask import request, jsonify
from ..models import *

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        try:
            assert request.form['username'] is not None, 'Username is required'
            assert request.form['password'] is not None, 'Password is required'

            u = User(username=request.form['username'])
            u.set_password(request.form['password'])

        except AssertionError as e:
            flash(e)

    return render_template('auth/register.jinja2')


@auth.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('auth/login.jinja2')

    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    #     db = get_db()
    #     error = None
    #     user = db.execute(
    #         'SELECT * FROM user WHERE username = ?', (username,)
    #     ).fetchone()
    #
    #     if user is None:
    #         error = 'Incorrect username.'
    #     elif not check_password_hash(user['password'], password):
    #         error = 'Incorrect password.'
    #
    #     if error is None:
    #         session.clear()
    #         session['user_id'] = user['id']
    #         return redirect(url_for('index'))
    #
    #     flash(error)
    #
    # return render_template('auth/login.html')
