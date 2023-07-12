#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData, create_engine, Table, Integer, String, Column, ForeignKey, DateTime, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Post(Base):
    __table__ = 'posts'
    id = Column(Integer, primary_key= True)
    title = Column(String(100), nullable=False)
    published = Column(String(200), nullable=False, unique=True)
    created_om = Column(DateTime(), default=datetime.now)
    updated_on = Column(datetime(), default=datetime.now, onupdate=datetime.now)
    
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('username')
    )