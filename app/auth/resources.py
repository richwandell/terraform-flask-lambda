import functools

from flask import Blueprint, redirect, url_for, session, g
from .models import User


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


auth = Blueprint('auth', __name__)

from .login import login
from .register import register
from .index import index


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.index'))




