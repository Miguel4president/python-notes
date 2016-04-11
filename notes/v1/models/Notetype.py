from marshmallow import Schema, fields, post_load
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from Tenant import TenantSchema, db


class Notetype(db.Model):
    __tablename__ = 'notetype'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_2_enabled = Column(Boolean, nullable=False)
    date_2_field_label = Column(String)
    site_visit = Column(Boolean, nullable=False)
    deal_issues = Column(Boolean, nullable=False)
    delete_lock_until = Column(DateTime)
    discussion_points = Column(JSON)

    # Foreign Keys
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    tenant = relationship("Tenant")

    def __init__(self, name, tenant_id, date_2_enabled, date_2_field_label, site_visit, deal_issues,
                 delete_lock_until, discussion_points):
        self.name = name
        self.tenant_id = tenant_id
        self.date_2_enabled = date_2_enabled
        self.date_2_field_label = date_2_field_label
        self.site_visit = site_visit
        self.deal_issues = deal_issues
        self.delete_lock_until = delete_lock_until
        self.discussion_points = discussion_points

    def __repr__(self):
        return '<Notetype: ' \
               ' id={0.id!r},' \
               ' name={0.name!r},' \
               ' tenant_id={0.tenant_id!r},' \
               ' date_2_enabled={0.date_2_enabled!r},' \
               ' date_2_field_label={0.date_2_field_label!r},' \
               ' site_visit={0.site_visit!r},' \
               ' deal_issues={0.deal_issues!r},' \
               ' delete_lock_until={0.delete_lock_until!r},' \
               ' discussion_points={0.discussion_points!r},'.format(self)


class NotetypeSchema(Schema):
    tenant = fields.Nested(TenantSchema)

    @post_load
    def make_notetype(self, data):
        return Notetype(**data)

    class Meta:
        fields = ("id",
                  "name",
                  "tenant",
                  "date_2_enabled",
                  "date_2_field_label",
                  "site_visit",
                  "deal_issues",
                  "delete_lock_until",
                  "discussion_points")

notetype_schema = NotetypeSchema()
notetypes_schema = NotetypeSchema(many=True)