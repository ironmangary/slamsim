# models/segment_type_model.py
# Version 2024.10.4.1
# For SlamSim

from db import db

class segment_type_model(db.Model):
    __tablename__ ='segment_type_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    suggested_length = db.Column(db.Integer)

    def __repr__(self):
        return f'segment_type_model({self.id}, {self.name})'
