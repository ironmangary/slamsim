# models/tag_team_model.py
# Version 2024.10.2.1
# For SlamSim

from db import db

class tag_team_model(db.Model):
    __tablename__ = 'tag_team_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pic = db.Column(db.String(100), nullable=True)
    type = db.Column(db.String(10), nullable=False)
    wrestler1_id = db.Column(db.Integer, db.ForeignKey('wrestler_table.id'), nullable=False)
    wrestler1 = db.relationship('wrestler_model', backref=db.backref('tag_teams1', lazy=True))
    wrestler2_id = db.Column(db.Integer, db.ForeignKey('wrestler_table.id'), nullable=False)
    wrestler2 = db.relationship('wrestler_model', backref=db.backref('tag_teams2', lazy=True))
    wrestler3_id = db.Column(db.Integer, db.ForeignKey('wrestler_table.id'), nullable=True)
    wrestler3 = db.relationship('wrestler_model', backref=db.backref('tag_teams3', lazy=True))
    status = db.Column(db.String(10), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'), nullable=True)
    league = db.relationship('league_model', backref=db.backref('tag_teams', lazy=True))
    manager_id = db.Column(db.Integer, db.ForeignKey('other_staff_table.id'), nullable=True)
    manager = db.relationship('other_staff_model', backref=db.backref('tag_teams', lazy=True))
    finisher1 = db.Column(db.String(100), nullable=False)
    finisher2 = db.Column(db.String(100), nullable=True)
    finisher3 = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    wins = db.Column(db.Integer, nullable=True)
    losses = db.Column(db.Integer, nullable=True)
    draws = db.Column(db.Integer, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'tag_team_model({self.id}, {self.name})'
        