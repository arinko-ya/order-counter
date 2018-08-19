from app import db
from app.genre.models import Genre
from app.utils.log_util import Result, Status


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    orders = db.relationship('Order', backref='item', lazy=True)

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
    def update(cls, id: int, name: str, genre: Genre,
               price: int, is_active: bool):
        before_item = cls.query.get(id)

        # 変更後の name が重複していたら failed を返す
        if before_item.name == name:
            pass
        elif cls.check_duplicate(name):
            return Result(Status.FAILED, f'{name} exists.')

        if not before_item:
            return Result(Status.FAILED, 'Item update is failed.')

        before_item.name = name
        before_item.genre = genre
        before_item.price = price
        before_item.is_active = is_active

        db.session.commit()

        return Result(Status.SUCCEEDED, 'Item update is complete!')

    @classmethod
    def get_sale_list(cls) -> list:
        return cls.query.filter_by(is_active=True).all()
