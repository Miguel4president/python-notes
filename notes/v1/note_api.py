import datetime

from flask import jsonify, Blueprint
from models import db, Note, note_schema, notes_schema

api_v1 = Blueprint('api_v1', __name__)


def get_date(day):
    return datetime.datetime(2011, 1, day, 10, 23)


def get_fake_note():
    note = Note(created_by='aaron', date=get_date(4), date_2=get_date(3), deal_issues="{ thing: 'va'}",
                discussion_points="{ another: { thing: 'va' }}", property_id=1, site_visit_id=6,
                text="Finally finished writting this!", tenant_id=1, notetype_id=4)
    return note


@api_v1.route('/notes', methods=['GET'])
def get_notes():
    all_notes = Note.query.all()

    result = notes_schema.dump(all_notes)
    return jsonify({'notes': result.data})


@api_v1.route('/notes', methods=['POST'])
def add_note():
    note = get_fake_note()
    db.session.add(note)
    db.session.commit()

    result = note_schema.dump(note)
    return jsonify({'note': result.data})


@api_v1.route('/notes/<id>', methods=['GET'])
def get_note(id):
    note = Note.query.filter_by(id=id).first()

    result = note_schema.dump(note)
    return jsonify({'note': result.data})


@api_v1.route('/notes/<id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.filter_by(id=id).first()
    db.session.delete(note)
    db.sessino.commit()
    return 'success'


@api_v1.route('/notes/<id>', methods=['PUT'])
def update_note():
    return 'not yet'






