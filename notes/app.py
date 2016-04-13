import os

from flask import Flask

from v1 import db, notetype_bp, note_bp, tenant_bp

app = Flask(__name__)

# Set what environment you want to run as
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(tenant_bp, url_prefix='/api/v1')
app.register_blueprint(note_bp, url_prefix='/api/v1/tenants/<tenant_id>')
app.register_blueprint(notetype_bp, url_prefix='/api/v1/tenants/<tenant_id>')

db.init_app(app)

if app.config.get('DEVELOPMENT') and not app.config.get('TESTING'):
    print app.url_map

if __name__ == '__main__':
    app.run()