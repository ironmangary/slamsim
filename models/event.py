# models/event_model.py
# Version 2024.10.3.1
# For SlamSim

from db import db

class event_model(db.Model):
    __tablename__ = 'event_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    episode_number = db.Column(db.Integer, nullable=True)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'), nullable=False)
    league = db.relationship('league_model', backref=db.backref('events', lazy=True))
    date = db.Column(db.Date, nullable=False)
    event_type = db.Column(db.String(20), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue_table.id'), nullable=True)
    venue = db.relationship('venue_model', backref=db.backref('events', lazy=True))

    def __repr__(self):
        return f'event_model({self.id}, {self.name})'
        