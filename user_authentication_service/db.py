#!/usr/bin/env python3
"""DB module
This module provides a DB class that handles interactions with a SQLite database.
It manages user data using SQLAlchemy ORM.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import User, Base


class DB:
    """DB class
    This class provides methods to interact with the database, such as adding and finding users.
    """

    def __init__(self) -> None:
        """Initialize a new DB instance.
        Creates a new SQLite database (if not already existing), and initializes the session.
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session: Session | None = None

    @property
    def _session(self) -> Session:
        """Memoized session object.
        Returns the current session or creates a new one if none exists.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the users table.
        
        Args:
            email (str): The email of the new user.
            hashed_password (str): The hashed password of the new user.

        Returns:
            User: The newly created user object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs: str) -> User:
        """Find the first user that matches the provided filter arguments.
        
        Args:
            **kwargs: Arbitrary keyword arguments for filtering the user.
        
        Returns:
            User: The first user found that matches the filters.

        Raises:
            InvalidRequestError: If no arguments are provided.
            NoResultFound: If no user matches the criteria.
        """
        if not kwargs:
            raise InvalidRequestError("No arguments provided for filtering.")

        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound("No user found matching the criteria.")

        return user
