from flask import jsonify, Blueprint, request
import query_helper

from models import db, Tenant

# This blueprint has an implied prefix of /api/v1/tenants/<tenant_id>
tenant_bp = Blueprint('tenant_bp', __name__)


# Json to Sql
def create_tenant_from_request(inc_request):
    data = inc_request.get_json()
    result = Tenant.tenant_schema.load(data)
    return result.data


# Sql to Json
def create_json(tenant):
    if isinstance(tenant, list):
        result = Tenant.tenants_schema.dump(tenant)
        return jsonify({'tenants': result.data})
    else:
        result = Tenant.tenant_schema.dump(tenant)
        return jsonify({'tenant': result.data})


@tenant_bp.route('/tenants', methods=['GET'])
def get_tenants():
    all_tenants = query_helper.get_tenants()

    return create_json(all_tenants)


@tenant_bp.route('/tenants', methods=['POST'])
def create_tenant():
    tenant = create_tenant_from_request(request)

    db.session.add(tenant)
    db.session.commit()

    return create_json(tenant)


@tenant_bp.route('/tenants/<id>', methods=['GET'])
def get_tenant(id):
    tenant = query_helper.get_tenant_by_id(id)

    return create_json(tenant)


@tenant_bp.route('/tenants/<id>', methods=['PUT'])
def update_tenant(id):
    tenant = create_tenant_from_request(request)
    tenant.id = id

    merged_tenant = db.session.merge(tenant)
    db.session.commit()

    return create_json(merged_tenant)


@tenant_bp.route('/tenants/<id>', methods=['DELETE'])
def delete_tenant(id):
    tenant = query_helper.get_tenant_by_id(id)
    db.session.delete(tenant)
    db.session.commit()
    return "Success"








