from flask import Blueprint, render_template
from flask import request, jsonify
from flask_graphql import GraphQLView

from .graphql import schema
from .oauth import oauth
from ..auth.resources import login_required
from .models import Client

api = Blueprint('api', __name__)


@api.route('/hello_lambda', methods=('GET', 'POST'))
def handle_artists():
    if request.method == 'POST':
        return 'ok'

    return jsonify([{'hi': 'from lambda'}])


@api.route('/oauth/authorize', methods=['GET', 'POST'])
@login_required
@oauth.authorize_handler
def authorize(*args, **kwargs):
    if request.method == 'GET':
        client_id = kwargs.get('client_id')
        client = Client.query.filter_by(client_id=client_id).first()
        kwargs['client'] = client
        return render_template('api/oauth_confirm.jinja2', **kwargs)

    confirm = request.form.get('confirm', 'no')
    return confirm == 'yes'


@api.route('/oauth/token')
@oauth.token_handler
def access_token():
    return None


def graphql_view():
    view = GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
    return login_required(view)


api.add_url_rule(
    '/graphql',
    view_func=graphql_view()
)