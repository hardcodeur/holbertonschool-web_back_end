#!/usr/bin/env python3
"""User module for ORM
This module defines the User class for SQLAlchemy ORM, representing a user in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User class
    This class represents the 'users' table in the database.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str | None = Column(String(250), nullable=True)
    reset_token: str | None = Column(String(250), nullable=True)
