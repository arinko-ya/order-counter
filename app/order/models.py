from app import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date_sold = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return f'<Order {self.item_id}>'

    def add_order(self, item_id, quantity):
        pass
