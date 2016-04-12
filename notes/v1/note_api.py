import query_helper
from flask import jsonify, Blueprint, request

from models import db
from models.Note import note_schema, notes_schema


# This blueprint has an implied prefix of /api/v1/tenants/<tenant_id>
note_bp = Blueprint('note_bp', __name__)


# JSON to SQL
def create_note_from_request(inc_request, tenant_id):
    data = inc_request.get_json()
    data['tenant_id'] = tenant_id

    if data.get('notetype'):
        data['notetype_id'] = data['notetype']['id']

    result = note_schema.load(data)
    return result.data


# SQL to JSON
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
    note = create_note_from_request(request, tenant_id)

    db.session.add(note)
    db.session.commit()

    return create_json(note)


@note_bp.route('/notes/<note_id>', methods=['GET'])
def get_note(tenant_id, note_id):
    note = query_helper.get_note_by_id(note_id)

    return create_json(note)


@note_bp.route('/notes/<id>', methods=['PUT'])
def update_note(tenant_id, id):
    note = create_note_from_request(request, tenant_id)
    note.id = id

    print "In note put method before merge"
    print note
    merged_note = db.session.merge(note)
    return create_json(merged_note)


@note_bp.route('/notes/<note_id>', methods=['DELETE'])
def delete_note(tenant_id, note_id):
    note = query_helper.get_note_by_id(note_id)
    db.session.delete(note)
    db.session.commit()

    return "Success"








