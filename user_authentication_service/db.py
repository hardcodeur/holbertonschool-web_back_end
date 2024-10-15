#!/usr/bin/env python3
"""DB module
This module provides a DB class to interact with the database using SQLAlchemy ORM.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User  # Import User model


class DB:
    """DB class to interact with the database.

    This class manages the database connection and provides methods
    for adding users to the database.
    """

    def __init__(self) -> None:
        """Initialize a new DB instance and set up the database.

        It creates a new SQLite database (if not existing), drops all
        tables to ensure a clean state, and initializes the session.
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session: Session | None = None

    @property
    def _session(self) -> Session:
        """Memoized session object to ensure only one session is used.

        Returns:
            Session: The current session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): The user's email address.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The newly created User object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        
        self._session.add(new_user)
        self._session.commit()
        
        return new_user
