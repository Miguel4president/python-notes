from flask import jsonify

from models import db, Notetype, notetype_schema, notetypes_schema
from note_api import api_v1


def get_fake_notetype():
    return Notetype('kewlType', False, site_visit=False, deal_issues=False, discussion_points='{ a: 2 }',
                    date_2_field_label="Words", delete_lock_until=None)


def create_json(notetype):
    if isinstance(notetype, list):
        result = notetypes_schema.dump(notetype)
        return jsonify({'notetypes': result.data})
    else:
        result = notetype_schema.dump(notetype)
        return jsonify({'notetype': result.data})


@api_v1.route('/notetypes', methods=['GET'])
def get_notetypes():
    all_notetypes = Notetype.query.all()

    return create_json(all_notetypes)


@api_v1.route('/notetypes', methods=['POST'])
def create_notetypes():
    notetype = get_fake_notetype()
    db.session.add(notetype)
    db.session.commit()

    return create_json(notetype)


@api_v1.route('/notetypes/<id>', methods=['GET'])
def get_notetype(id):
    notetype = Notetype.query.filter_by(id=id).first()

    return create_json(notetype)


@api_v1.route('/notetypes/<id>', methods=['PUT'])
def update_notetype():
    return 'not yet'


@api_v1.route('/notetypes/<id>', methods=['DELETE'])
def delete_notetype(id):
    notetype = Notetype.query.filter_by(id=id).first()
    db.session.delete(notetype)
    db.session.commit()
    return "success"