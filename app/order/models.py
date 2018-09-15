from collections import namedtuple
from datetime import datetime
from itertools import groupby

from app import db

OrderPerItem = namedtuple('OrderPerItem', ('sold_at', 'item', 'quantity', 'amount'))
OrderPerDay = namedtuple('OrderPerDay', ('sold_at', 'total_amount', 'order_list'))


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'),
                        nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sold_at = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Order {self.item_id}>'


class OrderHistory:
    @classmethod
    def sort_keys(cls, o):
        return datetime(o.sold_at.year, o.sold_at.month, o.sold_at.day), o.item.name

    @classmethod
    def calc(cls):
        order_list = Order.query.all()
        order_list.sort(key=cls.sort_keys, reverse=True)

        tmp_list = []
        for key, group in groupby(order_list, key=cls.sort_keys):
            group = list(group)

            total_quantity = sum(o.quantity for o in group)
            total_amount = sum(o.price for o in group)

            tmp_list.append(OrderPerItem(
                sold_at=key[0],
                item=key[1],
                quantity=total_quantity,
                amount=total_amount
            ))

        result_list = []
        for key, group in groupby(tmp_list, key=lambda o: o.sold_at):
            group = list(group)

            total_amount = sum(o.amount for o in group)

            result_list.append(OrderPerDay(
                sold_at=key,
                total_amount=total_amount,
                order_list=group
            ))

        return result_list
