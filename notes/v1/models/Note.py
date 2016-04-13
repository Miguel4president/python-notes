import datetime

from marshmallow import Schema, fields, post_load
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from Tenant import TenantSchema, db
from Notetype import NotetypeSchema


# 15 fields
class Note(db.Model):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, nullable=False)
    site_visit_id = Column(Integer)

    created_by = Column(String)
    text = Column(String)
    last_modified_by = Column(String)
    date_2_last_modified_by = Column(String)

    deal_issues = Column(JSON)
    discussion_points = Column(JSON)

    date = Column(DateTime)
    date_2 = Column(DateTime)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_last_modified = Column(DateTime, default=datetime.datetime.utcnow)
    date_2_last_modified = Column(DateTime, default=datetime.datetime.utcnow)

    # Foreign Keys
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    tenant = relationship("Tenant")

    notetype_id = Column(Integer, ForeignKey('notetype.id'))
    notetype = relationship("Notetype")

    def __repr__(self):
        return '<Note: ' \
               ' id={0.id!r},' \
               ' property_id={0.property_id!r},' \
               ' site_visit_id={0.site_visit_id!r},' \
               ' tenant_id={0.tenant_id!r},' \
               ' notetype_id={0.notetype_id!r},' \
               ' created_by={0.created_by!r},' \
               ' text={0.text!r},' \
               ' last_modified_by={0.last_modified_by!r},' \
               ' date_2_last_modified_by={0.last_modified_by!r},' \
               ' deal_issues={0.deal_issues!r},' \
               ' discussion_points={0.discussion_points!r},' \
               ' date={0.date!r},' \
               ' date_2={0.date_2!r},' \
               ' date_created={0.date_created!r},' \
               ' date_last_modified={0.date_last_modified!r},' \
               ' date_2_last_modified={0.date_2_last_modified!r}>'.format(self)


class NoteSchema(Schema):
    notetype_id = fields.Integer(load_only=True)

    notetype = fields.Nested(NotetypeSchema, dump_only=True)
    id = fields.Integer(dump_only=True)
    created_by = fields.String(dump_only=True)
    date_created = fields.DateTime(dump_only=True)
    date_last_modified = fields.DateTime(dump_only=True)
    date_2_last_modified = fields.DateTime(dump_only=True)
    date_2_last_modified_by = fields.DateTime(dump_only=True)

    @post_load
    def make_note(self, data):
        return Note(**data)

    class Meta:
        ordered = True
        additional = ("property_id",
                      "tenant_id",
                      "site_visit_id",
                      "text",
                      "deal_issues",
                      "discussion_points",
                      "date",
                      "date_2")

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)