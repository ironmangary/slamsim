# models/match_participants_model.py
# Version 2024.10.4.1
# For SlamSim

from db import db

class match_participants_model(db.Model):
    __tablename__ ='match_participants_table'

    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event_table.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('match_table.id'))
    wrestler_id = db.Column(db.Integer, db.ForeignKey('wrestler_table.id'))
    team_number = db.Column(db.Integer)
    member_num = db.Column(db.Integer)
    role = db.Column(db.String(50))  # e.g., 'winner', 'loser', 'challenger', etc.

    league = db.relationship('league_model', backref=db.backref('match_participants', lazy=True))
    event = db.relationship('event_model', backref=db.backref('match_participants', lazy=True))
    match = db.relationship('match_model', backref=db.backref('match_participants', lazy=True))
    wrestler = db.relationship('wrestler_model', backref=db.backref('match_participants', lazy=True))

    def __repr__(self):
        return f'match_participants_model({self.id}, {self.match_id}, {self.wrestler_id})'
        