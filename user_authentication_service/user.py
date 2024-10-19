#!/usr/bin/env python3
"""
User module for ORM.

This module defines the User class for SQLAlchemy ORM, representing a user in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User class representing the 'users' table in the database.

    Attributes:
        id (int): The primary key, automatically incremented.
        email (str): The user's email, which cannot be null.
        hashed_password (str): The user's hashed password, which cannot be null.
        session_id (str | None): The session ID associated with the user, nullable.
        reset_token (str | None): The reset token for password recovery, nullable.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
