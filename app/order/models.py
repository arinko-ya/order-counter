from datetime import datetime

from app import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'),
                        nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sold_at = db.Column(db.TIMESTAMP, nullable=False,
                        default=datetime.now().date())

    def __repr__(self):
        return f'<Order {self.item_id}>'

    def add_order(self, item_id, quantity):
        pass
