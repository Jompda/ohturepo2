from entities.user import User
import re
#import sys, pdb


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        #pdb.Pdb(stdout=sys.__stdout__).set_trace()

        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise UserInputError("Username must be at least 3 characters long")
        
        if re.match(r"^[a-z]+$", username) == None:
            raise UserInputError("Username must contain only letters a-z")
        
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")
        
        if re.match(r"^[a-z]+$", password) != None:
            raise UserInputError("Password may not only contain letters")
