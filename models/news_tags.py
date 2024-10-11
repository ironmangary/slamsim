# models/news_tags_model.py
# Version 2024.10.4.1
# For SlamSim

from db import db

class news_tags_model(db.Model):
    __tablename__ = 'news_tags_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f'news_tags_model({self.id}, {self.name})'
        