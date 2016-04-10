from flask import jsonify

from models.Tenant import db, Tenant, tenant_schema, tenants_schema
from note_api import api_v1


def get_fake_tenant():
    return Tenant(name="astar", public_key="asdr23f325DD")


@api_v1.route('/tenants', methods=['GET'])
def get_tenants():
    all_tenants = Tenant.query.all()

    result = tenants_schema.dump(all_tenants)
    return jsonify({'tenants': result.data})


@api_v1.route('/tenants', methods=['POST'])
def create_tenant():
    tenant = get_fake_tenant()
    db.session.add(tenant)
    db.session.commit()

    result = tenant_schema.dump(tenant)
    return jsonify({'tenant': result.data})


@api_v1.route('/tenants/<id>', methods=['GET'])
def get_tenant(id):
    tenant = Tenant.query.filter_by(id=id).first()

    result = tenant_schema.dump(tenant)
    return jsonify({'tenant': result.data})


@api_v1.route('/tenants/<id>', methods=['PUT'])
def update_tenant(id):
    return 'not yet, also should require admin priviledge'


@api_v1.route('/tenants/<id>', methods=['DELETE'])
def delete_tenant(id):
    return 'not yet, also should require admin priviledge'








