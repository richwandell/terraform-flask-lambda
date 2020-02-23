from flask_migrate import Migrate

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
    migrate = Migrate(app, db)

    return app
