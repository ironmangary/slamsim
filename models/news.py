# models/news_model.py
# Version 2024.10.4.1
# For SlamSim

from db import db

class news_model(db.Model):
    __tablename__ = 'news_table'

    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer, db.ForeignKey('league_table.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    league = db.relationship('league_model', backref=db.backref('news', lazy=True))
    tags = db.relationship('news_tags_model', backref=db.backref('news', lazy=True), secondary='news_tags_association_table')

    def __repr__(self):
        return f'news_model({self.id}, {self.league_id}, {self.date}, {self.title})'
