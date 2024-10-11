# models/venue_model.py
# Version 2024.10.2.1
# For SlamSim

from db import db

class venue_model(db.Model):
    __tablename__ ='venue_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pic = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    capacity = db.Column(db.Integer, nullable=True)
    bio = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'venue_model({self.id}, {self.name})'
        