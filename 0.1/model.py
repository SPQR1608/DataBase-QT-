from sqlalchemy import Column, ForeignKey, Integer, Float, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Category(Base):
    """
    Категория
    """
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    description = Column(Text())
    items = relationship('Item', backref='items')

    def __repr__(self):
        return '<Category> {}'.format(self.name)

    def __str__(self):
        return '<Category> {}'.format(self.name)


class Item(Base):
    """
    Товар
    """
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    id_category = Column(Integer, ForeignKey('category.id'))
    id_manufacturer = Column(Integer, ForeignKey('manufacturer.id'))
    name = Column(String(150))
    description = Column(Text())
    price = Column(Float)
    count = Column(Integer)

    def __repr__(self):
        return '<Item> {}'.format(self.name)

    def __str__(self):
        return '<Item> {}'.format(self.name)


class Manufacturer(Base):
    """
    Производитель
    """
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))

    def __repr__(self):
        return '<Manufacturer> {}'.format(self.name)

    def __str__(self):
        return '<Manufacturer> {}'.format(self.name)


class Order(Base):
    """
    Заказ
    """
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    id_item = Column(Integer, ForeignKey('item.id'))
    id_buyer = Column(Integer, ForeignKey('buyer.id'))

    def __repr__(self):
        return '<Order> {}'.format(self.id_item)

    def __str__(self):
        return '<Order> {}'.format(self.id_item)


class Buyer(Base):
    """
    Заказ
    """
    __tablename__ = 'buyer'
    id = Column(Integer, primary_key=True)
    nick = Column(String(150))
    email = Column(String(150))

    def __repr__(self):
        return '<Buyer> {}'.format(self.nick)

    def __str__(self):
        return '<Buyer> {}'.format(self.nick)
