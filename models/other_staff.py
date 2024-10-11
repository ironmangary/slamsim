# models/other_staff_model.py
# Version 2024.10.2.1
# For SlamSim

from db import db

class other_staff_model(db.Model):
    __tablename__ = 'other_staff_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'), nullable=True)
    league = db.relationship('league_model', backref=db.backref('other_staff', lazy=True))
    role = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    bio = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'other_staff_model({self.id}, {self.name})'
        