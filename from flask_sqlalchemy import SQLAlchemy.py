from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    batches_created = db.relationship('Batch', backref='creator', lazy=True)

class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime)

    audio_files = db.relationship('AudioFile', backref='batch', lazy=True)

class AudioFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    audio_path = db.Column(db.String(300), nullable=False)
    transcript = db.Column(db.Text)
    segments = db.Column(db.JSON)  # [{'start':, 'end':, 'text':, 'speaker':}]
    status = db.Column(db.String(20), default='pending')  # pending / reviewed
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'))
