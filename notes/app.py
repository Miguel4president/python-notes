import os

from flask import Flask

from v1 import api_v1, db
from v1.models import Tenant, Note, Notetype

app = Flask(__name__)

# Set what environment you want to run as
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(api_v1, url_prefix='/api/v1')

db.init_app(app)

print app.url_map

if __name__ == '__main__':
    app.run()