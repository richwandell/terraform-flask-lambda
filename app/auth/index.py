from typing import List
from flask import url_for, render_template, jsonify, g, get_flashed_messages
from .resources import auth, login_required


@auth.route('/')
@login_required
def index():
    return render_template('auth/index.jinja2')


@auth.route('/index/get_initial_data')
@login_required
def get_initial_data():
    from .models import User
    from ..api.models import Client
    user: User = g.user
    clients: List[Client] = Client.query.filter_by(user=user).all()
    return jsonify({
        'user': {
            'username': user.username
        },
        'app': {
            'url_for_auth_logout': url_for('auth.logout'),
            'url_for_auth_register': url_for('auth.register'),
            'url_for_auth_login': url_for('auth.login'),
            'flashed_messages': get_flashed_messages()
        },
        'clients': list(map(lambda x: {
            'name': x.name,
            'client_id': x.client_id,
            'client_secret': x.client_secret,
            'description': x.description
        }, clients))
    })