#!/usr/bin/env python3
"""
Auth module to handle user authentication logic with the database.
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


class Auth:
    """
    Auth class to interact with the authentication database.
    Methods:
        register_user: Registers a new user with an email and a password.
        get_user_from_session_id: Retrieves a user using the session ID.
        valid_login: Verifies if the login credentials are correct.
        create_session: Creates a new session for a user and returns
        the session ID.
        destroy_session: Removes the session ID from the user
        record.
        get_reset_password_token: Generates and returns a password
        reset token for the user.
        update_password: Updates the user's password using a valid
        reset token.
    """

    def __init__(self):
        """ Initializes the Auth class with a DB instance."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user if the email is not already in use.
        Args:
            email (str): The user's email.
            password (str): The user's password.
        Returns:
            User: The newly created user.
        Raises:
            ValueError: If the user already exists.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """ Validates if the provided login credentials are correct.
        Args:
            email (str): The user's email.
            password (str): The user's password.
        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        password_bytes = password.encode('utf-8')
        if not bcrypt.checkpw(password_bytes, user.hashed_password):
            return False
        return True

    def create_session(self, email: str) -> str:
        """
        Creates a new session for the user and returns the session ID.
        Args:
            email (str): The user's email.
        Returns:
            str | None: The session ID if the session is created,
            None otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Retrieves a user using their session ID.
        Args:
            session_id (str): The session ID of the user.
        Returns:
            User | None: The user object if found, or None if no user matches the session ID.
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        
        return user
    
    def destroy_session(self, user_id: str) -> None:
        """ Destroys a user's session by setting their session ID to None.
        Args:
            user_id (str): The user's ID.
        """
        self._db.update_user(user_id, session_id=None)


def _hash_password(password: str) -> bytes:
    """ Hashes a password using bcrypt.
    Args:password (str): The plain text password to hash.
    Returns:bytes: The hashed password.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


def _generate_uuid() -> str:
    """ Generates a new UUID string.
    Returns:
        str: The generated UUID.
    """
    return str(uuid.uuid4())
