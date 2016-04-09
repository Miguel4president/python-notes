import datetime
from sqlalchemy.dialects.postgresql import JSON
from flask.ext.sqlalchemy import SQLAlchemy
from marshmallow import Schema

db = SQLAlchemy()


class SimpleNote(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    creator = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    data = db.Column(JSON)

    def __init__(self, text, creator, date, data):
        self.text = text
        self.creator = creator
        self.date = date
        self.data = data

    def __repr__(self):
        return '<SimpleNote: creator={0.creator!r},' \
               ' date={0.date!r},' \
               ' text={0.text!r},' \
               ' data={0.data!r}>'.format(self)


class SimpleNoteSchema(Schema):
    class Meta:
        fields = ("id", "creator", "date", "text", "data")


sn_schema = SimpleNoteSchema()
sns_schema = SimpleNoteSchema(many=True)