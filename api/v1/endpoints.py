import datetime
from models.models import db, SimpleNote, sns_schema, sn_schema
# from models.ModelsSchema import sns_schema, sn_schema
from flask import Blueprint, jsonify


note_api = Blueprint('note_api', __name__)


@note_api.route('/test')
def hello():
    return "Hello World!"


@note_api.route('/', methods=['GET'])
def get_all_notes():
    all_notes = SimpleNote.query.all()

    result = sns_schema.dump(all_notes)
    return jsonify({'notes': result.data})


@note_api.route('/', methods=['POST'])
def add_a_fake_note():
    note = SimpleNote(text='bla blah blah', creator='aaron', date=datetime.datetime(2011, 1, 1, 10, 23), data="{ data: 'will this work3' }")
    db.session.add(note)
    db.session.commit()

    result = sn_schema.dump(note)
    return jsonify({'note': result.data})

@note_api.route('/<id>', methods=['GET'])
def get_note_with_id(id):
    note = SimpleNote.query.filter_by(id=id).first()

    result = sn_schema.dump(note)
    return jsonify({'note': result.data})


# @note_api.route('/api/v1/notes', methods=['PUT'])
# def put_note():
#     test_note = SimpleNote(text='bla blah blah', creator='aaron', date=datetime.datetime(2011, 1, 1, 10, 23))
#     db.session.add(test_note)
#     db.session.commit()
#     return 'yep, did a thing.'