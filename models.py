# models.py
# for SlamSim

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Wrestler

class Wrestler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    nickname = db.Column(db.String(60))
    height = db.Column(db.String(10))
    weight = db.Column(db.String(10))
    gender = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(100))
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=True)
    image = db.Column(db.String(200))
    alignment = db.Column(db.String(20), nullable=False)
    style = db.Column(db.String(50))
    card_level = db.Column(db.String(50), nullable=False)
    manager = db.Column(db.String(60))
    tagteam = db.Column(db.String(60))
    faction = db.Column(db.String(60))
    finisher1 = db.Column(db.String(100), nullable=False)
    finisher2 = db.Column(db.String(100))
    finisher3 = db.Column(db.String(100))
    standard1 = db.Column(db.String(100), nullable=False)
    standard2 = db.Column(db.String(100), nullable=False)
    standard3 = db.Column(db.String(100))
    standard4 = db.Column(db.String(100))
    standard5 = db.Column(db.String(100))
    extreme1 = db.Column(db.String(100))
    extreme2 = db.Column(db.String(100))
    extreme3 = db.Column(db.String(100))
    status = db.Column(db.String(10), nullable=False)
    bio = db.Column(db.Text)

# League

class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    abbreviation = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    headquarters = db.Column(db.String(100))
    owner = db.Column(db.String(50))
    year_created = db.Column(db.Integer)
    image = db.Column(db.String(200))
    description = db.Column(db.Text)
    wrestlers = db.relationship('Wrestler', backref='league', lazy=True)

# Tag-teams

class TagTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'standard' or 'trios'
    gender = db.Column(db.String(10), nullable=False)  # 'male', 'female', or 'mixed'
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'))  # Reference to League
    wrestler1_id = db.Column(db.Integer, db.ForeignKey('wrestler.id'))  # Reference to Wrestler
    wrestler2_id = db.Column(db.Integer, db.ForeignKey('wrestler.id'))  # Reference to Wrestler
    wrestler3_id = db.Column(db.Integer, db.ForeignKey('wrestler.id'))  # Reference to Wrestler (nullable for 'standard')
    manager = db.Column(db.String(60))
    finisher1 = db.Column(db.String(100), nullable=False)
    finisher2 = db.Column(db.String(100))
    finisher3 = db.Column(db.String(100))
    status = db.Column(db.String(10), nullable=False, default='active')  # 'active' or 'inactive'
    bio = db.Column(db.Text)
    
    league = db.relationship('League', backref='tag_teams')
    wrestler1 = db.relationship('Wrestler', foreign_keys=[wrestler1_id])
    wrestler2 = db.relationship('Wrestler', foreign_keys=[wrestler2_id])
    wrestler3 = db.relationship('Wrestler', foreign_keys=[wrestler3_id])