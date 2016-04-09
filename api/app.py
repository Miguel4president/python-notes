import os
from flask import Flask
from v1.models.Note import db
from v1.endpoints import note_api

app = Flask(__name__)

# Set what environment you want to run as
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(note_api, url_prefix='/notes')

db.init_app(app)

if __name__ == '__main__':
    app.run()