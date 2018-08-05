from app.auth.models import User
from app.genre.models import Genre
from app import db


def main():
    db.drop_all()
    db.create_all()
    User.create('admin', 'password')
    db.session.add_all([
        Genre(name='Alcohol'),
        Genre(name='Non Alcohol'),
        Genre(name='Food'),
        Genre(name='Other')
    ])
    db.session.commit()


if __name__ == '__main__':
    main()
