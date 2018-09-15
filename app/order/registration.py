from datetime import datetime

from app import db
from app.item.models import Item
from app.order.models import Order
from app.utils.log_util import Result, Status


def save_order(orders: list) -> Result:
    results = []
    for order in orders:
        results.append(
            _add(
                order.get('item'),
                order.get('quantity'),
                order.get('sold_at')
            )
        )

    results = [r.status for r in results]
    if Status.SUCCEEDED not in results:
        return Result(Status.FAILED, f'Order was not added.')

    return Result(Status.SUCCEEDED, f'Successfully added order.')


def _add(item: Item, quantity: str,
         sold_at: datetime.date) -> Result:
    quantity = int(quantity)
    if not quantity:
        return Result(Status.FAILED)

    db.session.add(Order(item=item, price=item.price * quantity,
                         quantity=quantity, sold_at=sold_at))
    db.session.commit()

    return Result(Status.SUCCEEDED)
