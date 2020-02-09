from flask import Blueprint
from flask import request, jsonify

api = Blueprint('api', __name__)


@api.route('/hello_lambda', methods=('GET', 'POST'))
def handle_artists():
    if request.method == 'POST':
        return 'ok'

    return jsonify([{'hi': 'from lambda'}])