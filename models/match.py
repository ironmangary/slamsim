# models/match_model.py
# Version 2024.10.4.1
# For SlamSim

from db import db

class match_model(db.Model):
    __tablename__ ='match_table'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event_table.id'), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'), nullable=False)
    name = db.Column(db.String(100))
    time_limit = db.Column(db.Integer)
    referee_id = db.Column(db.Integer, db.ForeignKey('staff_table.id'))
    championship_id = db.Column(db.Integer, db.ForeignKey('championship_table.id'))
    match_type_id = db.Column(db.Integer, db.ForeignKey('match_type_table.id'), nullable=False)
    summary = db.Column(db.Text)
    title_change = db.Column(db.Boolean, default=False)
    outcome = db.Column(db.String(100))
    length = db.Column(db.Integer)

    event = db.relationship('event_model', backref=db.backref('matches', lazy=True))
    league = db.relationship('league_model', backref=db.backref('matches', lazy=True))
    referee = db.relationship('other_staff_model', backref=db.backref('matches', lazy=True))
    championship = db.relationship('championship_model', backref=db.backref('matches', lazy=True))
    match_type = db.relationship('match_type_model', backref=db.backref('matches', lazy=True))

    def __repr__(self):
        return f'match_model({self.id}, {self.event_id}, {self.league_id})'
