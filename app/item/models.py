from app import db
from app.utils.log_util import Result, Status


class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(64), index=True,
                     unique=True, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    price = db.Column(db.Integer, nullable=False)
    is_sale = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'

    @classmethod
    def check_duplicate(cls, item_name: str) -> bool:
        return bool(cls.query.filter_by(name=item_name).first())

    @classmethod
    def add_item(cls, **item):
        if cls.check_duplicate(item['name']):
            return Result(Status.FAILED, '{name} exists.')

        db.session.add(cls(**item))
        db.session.commit()
        return Result(Status.SUCCEEDED, 'Successfully added item.')

    @classmethod
    def update(cls, id: int, name: str, genre_id: str,
               price: int, is_sale: bool):
        if cls.check_duplicate(name):
            return Result(Status.FAILED, '{name} exists.')

        before_item = cls.query.filter_by(id=id).first()

        if not before_item:
            return Result(Status.FAILED, 'Item update is failed.')

        before_item.name = name
        before_item.genre_id = int(genre_id)
        before_item.price = price
        before_item.is_sale = is_sale

        db.session.commit()

        return Result(Status.SUCCEEDED, 'Item update is complete!')

    @classmethod
    def get_sale_list(cls) -> list:
        return cls.query.filter_by(is_sale=True).all()
