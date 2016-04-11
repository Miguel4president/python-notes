#  Make sure that all the files have initialized and expose the db and api
from tenant_api import tenant_bp, db
from notetype_api import notetype_bp
from note_api import note_bp

