from flask import jsonify, Blueprint, request
import query_helper

from models import db, tenant_schema, tenants_schema

# This blueprint has an implied prefix of /api/v1/tenants/<tenant_id>
tenant_bp = Blueprint('tenant_bp', __name__)


def create_json(tenant):
    if isinstance(tenant, list):
        result = tenant_schema.dump(tenant)
        return jsonify({'tenants': result.data})
    else:
        result = tenants_schema.dump(tenant)
        return jsonify({'tenant': result.data})


@tenant_bp.route('/tenants', methods=['GET'])
def get_tenants():
    all_tenants = query_helper.get_tenants()

    return create_json(all_tenants)


@tenant_bp.route('/tenants', methods=['POST'])
def create_tenant():
    data = request.get_json()

    result = tenant_schema.load(data)
    tenant = result.data

    db.session.add(tenant)
    db.session.commit()

    return create_json(tenant)


@tenant_bp.route('/tenants/<id>', methods=['GET'])
def get_tenant(id):
    tenant = query_helper.get_tenant_by_id(id)

    return create_json(tenant)


@tenant_bp.route('/tenants/<id>', methods=['PUT'])
def update_tenant(id):
    return 'not yet, also should require admin priviledge'


@tenant_bp.route('/tenants/<id>', methods=['DELETE'])
def delete_tenant(id):
    tenant = query_helper.get_tenant_by_id(id)
    db.session.delete(tenant)
    db.session.commit()
    return create_json(tenant)








