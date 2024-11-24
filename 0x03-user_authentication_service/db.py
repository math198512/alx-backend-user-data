#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import TypeVar
from user import User, Base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        takes two required string arguments:
        email and hashed_password, and returns a User object.
        """
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Finds a user based on a set of filters.
        """
        keys = []
        values = []
        for key, value in kwargs.items():
            if hasattr(User, key):
                keys.append(getattr(User, key))
                values.append(value)
            else:
                raise InvalidRequestError()
        user = self._session.query(User).filter(
            tuple_(*keys).in_([tuple(values)])
        ).first()
        if user is None:
            raise NoResultFound()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates a user's information in the database.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: Arbitrary keyword arguments representing
                    the fields to update and their new values.

        Returns:
            None
        """
        user = self.find_user_by(id=user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(User, key):
                    user.key = value
                else:
                    raise ValueError
        self._session.commit()
