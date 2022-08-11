from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, \
     UniqueConstraint
from sqlalchemy.orm import relationship

from api.utils import EnumEx
from api.db_store import db


class NoteType(EnumEx):
    SINGLE = 1
    LIST = 2


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    username = Column(String(100), unique=True)
    password = Column(String(100))


class Folder(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    notes = relationship("Note", back_populates="folder", cascade="delete")

    UniqueConstraint('name', 'user_id')


class Note(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    folder_id = Column(Integer, ForeignKey("folder.id"), nullable=False)
    type = Column(Integer, nullable=False)
    is_public = Column(Boolean, default=False)

    folder = relationship("Folder", back_populates="notes")
    items = relationship(
        "NoteItem",
        back_populates="note",
        cascade="all, delete, merge, delete-orphan"
    )


class NoteItem(db.Model):
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey("note.id"), nullable=False)
    text_body = Column(String(100), unique=False)

    note = relationship('Note')
