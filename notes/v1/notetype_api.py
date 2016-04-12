from flask import jsonify, Blueprint, request
import query_helper

from models import db
from models.Notetype import notetype_schema, notetypes_schema

# This blueprint has an implied prefix of /api/v1/tenants/<tenant_id>
notetype_bp = Blueprint('notetype_bp', __name__)


# JSON to SQL
def create_notetype_from_request(inc_request, tenant_id):
    data = inc_request.get_json()

    data['tenant_id'] = tenant_id

    result = notetype_schema.load(data)
    return result.data


# SQL to JSON
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
    notetype = create_notetype_from_request(request, tenant_id)
    print notetype

    db.session.add(notetype)
    db.session.commit()

    return create_json(notetype)


@notetype_bp.route('/notetypes/<id>', methods=['GET'])
def get_notetype(tenant_id, id):
    notetype = query_helper.get_notetype_by_id(id)

    return create_json(notetype)


@notetype_bp.route('/notetypes/<id>', methods=['PUT'])
def update_notetype(tenant_id, id):
    notetype = create_notetype_from_request(request, tenant_id)

    notetype.id = id

    merged_notetype = db.session.merge(notetype)
    db.session.commit()

    return create_json(merged_notetype)


@notetype_bp.route('/notetypes/<id>', methods=['DELETE'])
def delete_notetype(tenant_id, id):
    notetype = query_helper.get_notetype_by_id(id)
    db.session.delete(notetype)
    db.session.commit()
    return "Success"