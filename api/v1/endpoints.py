import datetime
from models.Note import db, Note, note_schema, notes_schema
from flask import Blueprint, jsonify


note_api = Blueprint('note_api', __name__)


def get_date(day):
    return datetime.datetime(2011, 1, day, 10, 23)


def get_fake_note():
    note = Note(created_by='aaron', date=get_date(4), date_2=get_date(3), deal_issues="{ thing: 'va'}",
                discussion_points="{ another: { thing: 'va' }}", property_id=1, site_visit_id=6,
                text="Finally finished writting this!", tenant_id=1)
    return note


@note_api.route('/test')
def hello():
    return "Hello World!"


@note_api.route('/', methods=['GET'])
def get_all_notes():
    all_notes = Note.query.all()

    result = notes_schema.dump(all_notes)
    return jsonify({'notes': result.data})


@note_api.route('/', methods=['POST'])
def add_a_fake_note():
    note = get_fake_note()
    db.session.add(note)
    db.session.commit()

    result = note_schema.dump(note)
    return jsonify({'note': result.data})


@note_api.route('/<id>', methods=['GET'])
def get_note_with_id(id):
    note = Note.query.filter_by(id=id).first()

    result = note_schema.dump(note)
    return jsonify({'note': result.data})




