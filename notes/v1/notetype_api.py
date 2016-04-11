from flask import jsonify, Blueprint, request
import query_helper

from models import db, Notetype, notetype_schema, notetypes_schema

# This blueprint has an implied prefix of /api/v1/tenants/<tenant_id>
notetype_bp = Blueprint('notetype_bp', __name__)


def get_fake_notetype():
    return Notetype(name='kewlType', site_visit=False, deal_issues=False, discussion_points='{ a: 2 }',
                    date_2_field_label="Words", delete_lock_until=None, date_2_enabled=False, tenant_id=1)


def create_json(notetype):
    if isinstance(notetype, list):
        result = notetypes_schema.dump(notetype)
        return jsonify({'notetypes': result.data})
    else:
        result = notetype_schema.dump(notetype)
        return jsonify({'notetype': result.data})


@notetype_bp.route('/notetypes', methods=['GET'])
def get_notetypes(tenant_id):
    all_notetypes = query_helper.get_notetypes_by_tenant(tenant_id)

    return create_json(all_notetypes)


@notetype_bp.route('/notetypes', methods=['POST'])
def create_notetypes(tenant_id):
    data = request.get_json()
    result = notetypes_schema.load(data)
    notetype = result.data

    db.session.add(notetype)
    db.session.commit()

    return create_json(notetype)


@notetype_bp.route('/notetypes/<id>', methods=['GET'])
def get_notetype(tenant_id, id):
    notetype = query_helper.get_notetype_by_id(id)

    return create_json(notetype)


@notetype_bp.route('/notetypes/<id>', methods=['PUT'])
def update_notetype(tenant_id, id):
    return 'not yet'


@notetype_bp.route('/notetypes/<id>', methods=['DELETE'])
def delete_notetype(tenant_id, id):
    notetype = query_helper.get_notetype_by_id(id)
    db.session.delete(notetype)
    db.session.commit()
    return create_json(notetype)