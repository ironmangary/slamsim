# models/segment_model.py
# Version 2024.10.4.1
# For SlamSim

from db import db

class segment_model(db.Model):
    __tablename__ ='segment_table'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event_table.id'), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'), nullable=False)
    segment_type_id = db.Column(db.Integer, db.ForeignKey('segment_type_table.id'), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.Text, nullable=False)

    event = db.relationship('event_model', backref=db.backref('segments', lazy=True))
    league = db.relationship('league_model', backref=db.backref('segments', lazy=True))
    segment_type = db.relationship('segment_type_model', backref=db.backref('segments', lazy=True))

    def __repr__(self):
        return f'segment_model({self.id}, {self.event_id}, {self.league_id}, {self.segment_type_id})'
        