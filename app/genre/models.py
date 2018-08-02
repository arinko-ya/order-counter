from app import db
from app.item.models import Item


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)

    item = db.relation(Item, backref=db.backref('genre', lazy=True))

    def __repr__(self):
        return f'<Genre {self.name}>'

    @classmethod
    def check_duplicate(cls, genre_name: str) -> bool:
        return bool(cls.query.filter_by(name=genre_name).first())

    @classmethod
    def add_genre(cls, genre_name: str):
        if cls.check_duplicate(genre_name):
            return 'NG', f'{genre_name} exists.'

        if cls.query.filter_by(name=genre_name).first():
            return 'NG', f'{genre_name} exists.'

        db.session.add(cls(name=genre_name))
        db.session.commit()

        return 'OK', 'Successfully added genre.'

    @classmethod
    def get_genre_list(cls) -> list:
        genre_list = cls.query.all()
        if genre_list:
            return [(str(g.id), g.name) for g in genre_list]
        return [('no_genre_table', 'no_genre_table')]

    @classmethod
    def update(cls, genre_id: str, genre_name: str):
        genre = cls.query.filter_by(id=genre_id).first()
        if genre:
            genre.name = genre_name
            db.session.commit()

            return 'Genre update is complete!'

        return 'Genre update is failed.'
