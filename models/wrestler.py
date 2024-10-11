# models/wrestler_model.py
# Version 2024.10.2.1
# For SlamSim

from db import db

class wrestler_model(db.Model):
    __tablename__ = 'wrestler_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pic = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(10), nullable=False)
    nickname = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(10), nullable=False)
    hometown = db.Column(db.String(100), nullable=True)
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    alignment = db.Column(db.String(10), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'), nullable=True)
    league = db.relationship('league_model', backref=db.backref('wrestlers', lazy=True))
    tag_team_id = db.Column(db.Integer, db.ForeignKey('tag_team_table.id'), nullable=True)
    tag_team = db.relationship('tag_team_model', backref=db.backref('wrestlers', lazy=True))
    faction_id = db.Column(db.Integer, db.ForeignKey('faction_table.id'), nullable=True)
    faction = db.relationship('faction_model', backref=db.backref('wrestlers', lazy=True))
    manager_id = db.Column(db.Integer, db.ForeignKey('other_staff_table.id'), nullable=True)
    manager = db.relationship('other_staff_model', backref=db.backref('wrestlers', lazy=True))
    level = db.Column(db.String(10), nullable=False)
    style = db.Column(db.String(10), nullable=True)
    finisher1 = db.Column(db.String(100), nullable=False)
    finisher2 = db.Column(db.String(100), nullable=True)
    finisher3 = db.Column(db.String(100), nullable=True)
    standard1 = db.Column(db.String(100), nullable=False)
    standard2 = db.Column(db.String(100), nullable=False)
    standard3 = db.Column(db.String(100), nullable=True)
    standard4 = db.Column(db.String(100), nullable=True)
    standard5 = db.Column(db.String(100), nullable=True)
    extreme1 = db.Column(db.String(100), nullable=True)
    extreme2 = db.Column(db.String(100), nullable=True)
    extreme3 = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    singles_wins = db.Column(db.Integer, nullable=True)
    singles_losses = db.Column(db.Integer, nullable=True)
    singles_draws = db.Column(db.Integer, nullable=True)
    tag_wins = db.Column(db.Integer, nullable=True)
    tag_losses = db.Column(db.Integer, nullable=True)
    tag_draws = db.Column(db.Integer, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'wrestler_model({self.id}, {self.name})'
        