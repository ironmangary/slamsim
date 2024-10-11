# models/match_type_model.py
# Version 2024.10.4.1
# For SlamSim

from db import db

class match_type_model(db.Model):
    __tablename__ ='match_type_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number_per_team = db.Column(db.Integer, nullable=False)
    number_teams = db.Column(db.Integer, nullable=False)
    suggested_time_limit = db.Column(db.Integer)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'match_type_model({self.id}, {self.name})'
        