from datetime import datetime

from app import db
from app.auth.models import User
from app.genre.models import Genre
from app.item.models import Item
from app.order.models import Order


def main():
    db.drop_all()
    db.create_all()

    User.create('admin', 'password')

    db.session.add_all([
        Genre(name='アルコール'),
        Genre(name='ノンアルコール'),
        Genre(name='フード'),
        Genre(name='その他')
    ])

    alcohol = Genre.query.filter_by(name='アルコール').first()
    non_alcohol = Genre.query.filter_by(name='ノンアルコール').first()
    food = Genre.query.filter_by(name='フード').first()
    etc = Genre.query.filter_by(name='その他').first()

    db.session.add_all([
        Item(name='凍結レモンサワー', genre=alcohol, price=590, is_active=True),
        Item(name='ほろ酔いカクテル', genre=alcohol, price=550, is_active=True),
        Item(name='バラエティサワー', genre=alcohol, price=550, is_active=True),
        Item(name='プレミアムモルツ', genre=alcohol, price=490, is_active=True),
        Item(name='メガビームハイ', genre=alcohol, price=660, is_active=True),
        Item(name='アイスコーヒー', genre=non_alcohol, price=300, is_active=True),
        Item(name='ジャスミンティー', genre=non_alcohol, price=300, is_active=True),
        Item(name='グレープフルーツジュース', genre=non_alcohol, price=340, is_active=True),
        Item(name='オレンジジュース', genre=non_alcohol, price=340, is_active=True),
        Item(name='アイスココア', genre=non_alcohol, price=330, is_active=True),
        Item(name='タコとアボカドの和風マリネ', genre=food, price=520, is_active=True),
        Item(name='切り落としローストビーフ', genre=food, price=680, is_active=True),
        Item(name='紫キャベツのビタミンサラダ', genre=food, price=400, is_active=True),
        Item(name='クリームチーズと蜂蜜ナッツ', genre=food, price=390, is_active=True),
        Item(name='鉄板餃子', genre=food, price=500, is_active=True),
        Item(name='スマイル・アゲイン', genre=etc, price=0, is_active=True),
    ])

    item_1 = Item.query.get(1)
    item_2 = Item.query.get(6)
    item_3 = Item.query.get(11)
    item_4 = Item.query.get(16)

    db.session.add_all([
        Order(item=item_1, price=item_1.price * 10, quantity=10, sold_at=datetime(2018, 8, 1, 18, 0, 0)),
        Order(item=item_2, price=item_2.price * 5, quantity=5, sold_at=datetime(2018, 8, 1, 18, 0, 0)),
        Order(item=item_3, price=item_3.price * 1, quantity=1, sold_at=datetime(2018, 8, 1, 18, 0, 0)),
        Order(item=item_4, price=item_4.price * 10, quantity=10, sold_at=datetime(2018, 8, 1, 18, 0, 0)),
        Order(item=item_1, price=item_1.price * 20, quantity=20, sold_at=datetime(2018, 8, 1, 19, 0, 0)),
        Order(item=item_2, price=item_2.price * 1, quantity=1, sold_at=datetime(2018, 8, 1, 19, 0, 0)),
        Order(item=item_3, price=item_3.price * 2, quantity=2, sold_at=datetime(2018, 8, 1, 19, 0, 0)),
        Order(item=item_4, price=item_4.price * 3, quantity=3, sold_at=datetime(2018, 8, 1, 19, 0, 0)),
        Order(item=item_1, price=item_1.price * 4, quantity=4, sold_at=datetime(2018, 8, 3, 18, 0, 0)),
        Order(item=item_2, price=item_2.price * 9, quantity=9, sold_at=datetime(2018, 8, 3, 18, 0, 0)),
        Order(item=item_3, price=item_3.price * 12, quantity=12, sold_at=datetime(2018, 8, 3, 18, 0, 0)),
        Order(item=item_4, price=item_4.price * 3, quantity=3, sold_at=datetime(2018, 3, 3, 18, 0, 0)),
        Order(item=item_1, price=item_1.price * 2, quantity=2, sold_at=datetime(2018, 8, 3, 19, 0, 0)),
        Order(item=item_2, price=item_2.price * 10, quantity=10, sold_at=datetime(2018, 8, 3, 19, 0, 0)),
        Order(item=item_3, price=item_3.price * 5, quantity=5, sold_at=datetime(2018, 8, 3, 19, 0, 0)),
        Order(item=item_4, price=item_4.price * 5, quantity=5, sold_at=datetime(2018, 8, 3, 19, 0, 0)),
        Order(item=item_1, price=item_1.price * 5, quantity=5, sold_at=datetime(2018, 8, 3, 21, 0, 0)),
        Order(item=item_2, price=item_2.price * 3, quantity=3, sold_at=datetime(2018, 8, 3, 21, 0, 0)),
        Order(item=item_3, price=item_3.price * 2, quantity=2, sold_at=datetime(2018, 8, 3, 21, 0, 0)),
        Order(item=item_4, price=item_4.price * 1, quantity=1, sold_at=datetime(2018, 8, 3, 21, 0, 0)),
    ])

    db.session.commit()


if __name__ == '__main__':
    main()
