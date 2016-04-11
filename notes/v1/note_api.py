import datetime
import query_helper

from flask import jsonify, Blueprint
from models import db, Note, note_schema, notes_schema


# This blueprint has an implied prefix of /api/v1/tenants/<tenant_id>
note_bp = Blueprint('note_bp', __name__)


def get_date(day):
    return datetime.datetime(2011, 1, day, 10, 23)


def get_fake_note():
    note = Note(created_by='aaron', date=get_date(4), date_2=get_date(3), deal_issues="{ thing: 'va'}",
                discussion_points="{ another: { thing: 'va' }}", property_id=1, site_visit_id=6,
                text="Finally finished writting this!", tenant_id=1, notetype_id=4)
    return note


def create_json(note):
    if isinstance(note, list):
        result = notes_schema.dump(note)
        return jsonify({'notes': result.data})
    else:
        result = note_schema.dump(note)
        return jsonify({'note': result.data})


@note_bp.route('/notes', methods=['GET'])
def get_notes(tenant_id):
    all_notes = query_helper.get_notes_by_tenant_id(tenant_id)

    return create_json(all_notes)


@note_bp.route('/notes', methods=['POST'])
def add_note(tenant_id):
    note = get_fake_note()
    note.tenant_id = tenant_id
    db.session.add(note)
    db.session.commit()

    return create_json(note)


@note_bp.route('/notes/<note_id>', methods=['GET'])
def get_note(tenant_id, note_id):
    note = query_helper.get_note_by_id(note_id)

    return create_json(note)


@note_bp.route('/notes/<note_id>', methods=['DELETE'])
def delete_note(tenant_id, note_id):
    note = query_helper.get_note_by_id(note_id)
    db.session.delete(note)
    db.sessino.commit()

    return create_json(note)


@note_bp.route('/notes/<id>', methods=['PUT'])
def update_note(tenant_id, note_id):
    return 'not yet'






