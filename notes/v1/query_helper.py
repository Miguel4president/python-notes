from models.Note import Note
from models.Notetype import Notetype
from models.Tenant import Tenant, db


# Note Queries
def get_note_by_id(note_id):
    return Note.query.filter_by(id=note_id).first()


def get_notes_by_tenant_id(tenant_id):
    return Note.query.filter_by(tenant_id=tenant_id).all()


def get_notes_by_tenant_name(tenant_name):
    return db.Session.query(Note, Tenant).filter(Note.tenant_id == Tenant.id). \
        filter(Tenant.name == tenant_name).all()


def get_notes_by_noteype_id(notetype_id):
    return db.Session.query(Note, Notetype).filter(Note.notetype_id == Notetype.id). \
        filter(Notetype.id == notetype_id).all()


def get_notes_by_notetype_name(notetype_name):
    return db.Session.query(Note, Notetype).filter(Note.notetype_id == Notetype.id). \
        filter(Notetype.name == notetype_name).all()


# Notetype Queries
def get_notetype_by_id(notetype_id):
    return Notetype.query.filter_by(id=notetype_id).first()


def get_notetype_by_name(notetype_name):
    return Notetype.query.filter_by(name=notetype_name).first()


def get_notetypes_by_tenant(tenant_id):
    return Notetype.query.filter_by(tenant_id=tenant_id).all()


# Tenant Queries
def get_tenants():
    return Tenant.query.all()


def get_tenant_by_id(tenant_id):
    return Tenant.query.filter_by(id=tenant_id).first()


def get_tenant_by_name(tenant_name):
    return Tenant.query.filter_by(name=tenant_name).first()


