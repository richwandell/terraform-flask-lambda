from flask_migrate import Migrate
from flask_session import Session

import config, os


def create_app(Flask):
    environment = os.environ.get('FLASK_ENV')
    app = Flask(__name__)
    from .api import api as api_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(api_blueprint)
    app.register_blueprint(auth_blueprint)
    app.config.from_object(config.LocalConfig if environment == "development" else config.BaseConfig)

    from .models import db
    db.init_app(app)
    Migrate(app, db)
    Session(app)

    from .api.oauth import oauth
    oauth.init_app(app)

    return app
