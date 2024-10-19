#!/usr/bin/env python3
"""
Database module for Object Relational Mapping (ORM) using SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from user import Base, User


class DB:
    """
    DB class for handling interactions with the database through ORM.
    
    Methods:
        add_user: Adds a new user to the database.
        find_user_by: Finds a user in the database by specific keyword arguments.
        update_user: Updates a user's attributes in the database.
    """

    def __init__(self):
        """Constructor method for initializing the database engine and session."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)  # Drops all tables and re-creates them
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """
        Creates and returns a new session if none exists.
        
        Returns:
            Session: The current session for database operations.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a new user to the database with the provided email and hashed password.
        
        Args:
            email (str): The user's email address.
            hashed_password (str): The hashed version of the user's password.
        
        Returns:
            User: The created User object.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user in the database using keyword arguments for filtering.
        
        Args:
            **kwargs: Arbitrary keyword arguments to filter the User table.
        
        Returns:
            User: The first user found that matches the criteria.
        
        Raises:
            InvalidRequestError: If no valid keyword arguments are provided or the keys are invalid.
            NoResultFound: If no user matches the provided criteria.
        """
        if not kwargs:
            raise InvalidRequestError("No keyword arguments provided for search")

        column_names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in column_names:
                raise InvalidRequestError(f"Invalid column: {key}")

        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound()

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates the attributes of a user in the database.
        
        Args:
            user_id (int): The ID of the user to update.
            **kwargs: The attributes to update for the user.
        
        Returns:
            None
        
        Raises:
            InvalidRequestError: If no valid keyword arguments are provided or if keys are invalid.
        """
        if not kwargs:
            raise InvalidRequestError("No fields to update provided")

        column_names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in column_names:
                raise InvalidRequestError(f"Invalid column: {key}")

        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            setattr(user, key, value)

        self._session.commit()
