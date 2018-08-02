from app import db


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

    def __init__(self, name: str, genre_id: str, price: int, is_sale: bool):
        self.name = name
        self.genre_id = int(genre_id)
        self.price = price
        self.is_sale = is_sale

    @classmethod
    def update(cls, id: int, name: str, genre_id: str,
               price: int, is_sale: bool):
        before_item = cls.query.filter_by(id=id).first()

        before_item.name = name
        before_item.genre_id = int(genre_id)
        before_item.price = price
        before_item.is_sale = is_sale

        db.session.commit()

    @classmethod
    def get_sale_list(cls) -> list:
        return cls.query.filter_by(is_sale=True).all()
