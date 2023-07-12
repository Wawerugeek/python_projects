#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, CheckConstraint, Insert
from datetime import datetime 

engine = create_engine("mysql+mysqldb://root:@localhost/my_data")
conn = engine.connect()

metadata = MetaData()

customers = Table('customers', metadata,
    Column('id', Integer(), primary_key=True),
    Column('first_name', String(100), nullable=False),
    Column('last_name', String(100), nullable=False),
    Column('username', String(50), nullable=False),
    Column('email', String(200), nullable=False),
    Column('address', String(200), nullable=False),
    Column('town', String(50), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)


items = Table('items', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(200), nullable=False),
    Column('cost_price', Numeric(10, 2), nullable=False),
    Column('selling_price', Numeric(10, 2),  nullable=False),
    Column('quantity', Integer(), nullable=False),
    CheckConstraint('quantity > 0', name='quantity_check')
)


orders = Table('orders', metadata,
    Column('id', Integer(), primary_key=True),
    Column('customer_id', ForeignKey('customers.id')),
    Column('date_placed', DateTime(), default=datetime.now),
    Column('date_shipped', DateTime())
)


order_lines = Table('order_lines', metadata,
    Column('id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.id')),
    Column('item_id', ForeignKey('items.id')),
    Column('quantity', Integer())
)

metadata.create_all(engine)

def create_customer():
    ins = Insert(customers)
    r = conn.execute(ins, [
        {
            "first_name" : 'john',
            "last_name" :'steve',
            "username" : 'johnsteve',
            "email" : "somerandom@gmail.com",
            "address" : ' 7974, tyw',
            "town" : 'Norfolk'  
        },
        {
          "first_name": "Sarah", 
            "last_name": "Tomlin", 
            "username": "sarahtomlin", 
            "email":"sarahtomlin@mail.com",
            "address": "3572 Poplar Avenue",
            "town": "Norfolk"  
        }, 
        {
            "first_name": "Pablo", 
            "last_name": "Gibson", 
            "username": "pablogibson", 
            "email":"pablogibson@mail.com",
            "address": "3494 Murry Street",
            "town": "Peterbrugh"
        },
        {
            "first_name": "Pablo", 
            "last_name": "Lewis", 
            "username": "pablolewis", 
            "email":"pablolewis@mail.com",
            "address": "3282 Jerry Toth Drive",
            "town": "Peterbrugh"
        }
        
    ])
    conn.commit()
    

create_customer()
create_items()
conn.close()
