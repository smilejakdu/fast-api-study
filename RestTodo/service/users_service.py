from fastapi import Depends

from RestTodo.repository.users_repository import UserRepository


class UserService():
    def __int__(self, repository: UserRepository = Depends()) -> None:
        self.repository = repository

    def find_user_by_id(self, user_id: int):
        return self.repository.find_user_by_id(user_id)
