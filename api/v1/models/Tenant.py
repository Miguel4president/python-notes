from sqlalchemy import Column, String, Integer
from marshmallow import Schema

from Database import db


class Tenant(db.Model):
    __tablename__ = 'site'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    public_key = Column(String, nullable=False)

    def __init__(self, name, public_key):
        self.name = name
        self.public_key = public_key

    def __repr__(self):
        return '<Tenant: ' \
               ' id={0.id!r},' \
               ' name={0.name!r},' \
               ' public_key={0.public_key!r}>,'.format(self)


class TenantSchema(Schema):
    class Meta:
        fields = ("id",
                  "name",
                  "public_key")

tenants_schema = TenantSchema(many=True)
tenant_schema = TenantSchema()
