# models/division_model.py
# Version 2024.10.2.1
# For SlamSim

from db import db

class division_model(db.Model):
    __tablename__ = 'division_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'), nullable=True)
    league = db.relationship('league_model', backref=db.backref('divisions', lazy=True))
    type = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'division_model({self.id}, {self.name})'
        