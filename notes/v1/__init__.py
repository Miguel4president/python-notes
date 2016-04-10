#  Make sure that all the files have initialized and expose the db and api

import note_api
import notetype_api
import tenant_api

from tenant_api import db, api_v1

