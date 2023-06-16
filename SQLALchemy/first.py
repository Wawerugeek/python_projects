#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData, Table, String, Column, Text, DateTime, Boolean, Integer
from datetime import datetime

engine = create_engine("mysql+mysqldb://root:@localhost/my_data")
engine.connect()

metadata = MetaData()

blog = Table ('blog', metadata,
              Column('id', Integer(), primary_key=True),
              Column('post_title', String(200), nullable=False),
              Column('post_slug', String(200), nullable=False),
              Column('content', Text(), nullable=False),
              Column("published", Boolean(), default=False),
              Column("Created_on", DateTime(), default=datetime.now),
              Column("updated_on", DateTime(), default=datetime.now, onupdate=datetime.now)
              )

metadata.create_all(engine)
