from fastapi import Depends
from sqlalchemy.orm import Session

from RestTodo.config.database import get_db
from RestTodo.entity.users_entity import Users


class UserRepository:
    def __int__(self, db_session: Session = Depends(get_db)) -> None:
        self.db = db_session

    def find_user_by_id(self, user_id: int):
        print(user_id)
        return self.db.query(Users).get({'id': user_id})
