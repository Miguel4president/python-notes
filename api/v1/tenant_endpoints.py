from models.Database import db
from models.Tenant import Tenant, tenant_schema, tenants_schema
from flask import Blueprint, jsonify


tenant_api = Blueprint('tenant_api', __name__)


def get_fake_tenant():
    return Tenant(name="astar", public_key="asdr23f325DD")


@tenant_api.route('/test')
def hello():
    return "Hello World!"


@tenant_api.route('/', methods=['GET'])
def get_all_tenants():
    all_tenants = Tenant.query.all()

    result = tenants_schema.dump(all_tenants)
    return jsonify({'tenants': result.data})


@tenant_api.route('/', methods=['POST'])
def add_a_fake_tenant():
    tenant = get_fake_tenant()
    db.session.add(tenant)
    db.session.commit()

    result = tenant_schema.dump(tenant)
    return jsonify({'tenant': result.data})


@tenant_api.route('/<id>', methods=['GET'])
def get_note_with_id(id):
    tenant = Tenant.query.filter_by(id=id).first()

    result = tenant_schema.dump(tenant)
    return jsonify({'tenant': result.data})




