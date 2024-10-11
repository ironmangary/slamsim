# models/event_card_model.py
# Version 2024.10.3.1
# For SlamSim

from db import db

class event_card_model(db.Model):
    __tablename__ = 'event_card_table'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event_table.id'), nullable=False)
    item_id = db.Column(db.Integer, nullable=False)  # This will hold the ID of either match or segment
    item_type = db.Column(db.String(50), nullable=False)  # 'match' or 'segment'
    order = db.Column(db.Integer, nullable=False)  # Position in the card
    
    event = db.relationship('event_model', backref=db.backref('event_items', lazy=True, cascade="all, delete-orphan"), lazy='dynamic')

    __table_args__ = (db.UniqueConstraint('event_id', 'order', name='_event_order_uc'),)

    def __repr__(self):
        return f'event_card_model({self.id}, event_id={self.event_id}, item_id={self.item_id}, item_type={self.item_type}, order={self.order})'
