# models/championship_model.py
# Version 2024.10.2.1
# For SlamSim

from db import db

class championship_model(db.Model):
    __tablename__ = 'championship_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pic = db.Column(db.String(100), nullable=True)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'), nullable=True)
    league = db.relationship('league_model', backref=db.backref('championships', lazy=True))
    division_id = db.Column(db.Integer, db.ForeignKey('division_table.id'), nullable=True)
    division = db.relationship('division_model', backref=db.backref('championships', lazy=True))
    rank = db.Column(db.Integer, nullable=True)
    current_champ_id = db.Column(db.Integer, db.ForeignKey('wrestler_table.id'), nullable=True)
    current_champ_wrestler = db.relationship('wrestler_model', backref=db.backref('championships_wrestler', lazy=True))
    current_champ_tag_team_id = db.Column(db.Integer, db.ForeignKey('tag_team_table.id'), nullable=True)
    current_champ_tag_team = db.relationship('tag_team_model', backref=db.backref('championships_tag_team', lazy=True))
    current_champ_status = db.Column(db.String(10), nullable=False, default='vacant')

    def __repr__(self):
        return f'championship_model({self.id}, {self.name})'
        