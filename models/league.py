# models/league.py
# Version 2024.10.2
# For SlamSim

from db import db

class league_model(db.Model):
    __tablename__ = 'league_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    abbreviation = db.Column(db.String(10), nullable=False)
    logo = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(10), nullable=False)
    owner = db.Column(db.String(100), nullable=True)
    headquarters = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'league_model({self.id}, {self.name})'
        