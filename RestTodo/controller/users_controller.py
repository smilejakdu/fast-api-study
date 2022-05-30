from fastapi import Depends, APIRouter
from fastapi_router_controller import Controller
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from RestTodo.config.database import engine, Base
from RestTodo.entity.users_entity import Users
from RestTodo.service.users_service import UserService
from RestTodo.shared.CoreResponse import not_found_response, internal_server_error
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base.metadata.create_all(bind=engine)
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/users",
    tags=["/users"],
    responses={404: {"user": "Not authorized"}},
)
controller = Controller(router, openapi_tag={
    'name': 'users-controller',
})


@controller.use()
@controller.resource()
class UserController:
    def __int__(
            self,
            service: UserService = Depends()) -> None:
        self.service = service

    @controller.router.get(
        '',
        tags=['users-controller'],
        summary='find user  from user table',
        status_code=200,
        response_model=Users,
    )
    async def find_user_by_id(
            self,
            user_id: int):
        try:
            found_user = self.service.find_user_by_id(user_id)
            if found_user is None:
                return not_found_response(user_id)

            return found_user
        except Exception:
            return internal_server_error()

# @router.post("/create/user")
# async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
#     create_user_model = Users()
#     create_user_model.email = create_user.email
#     create_user_model.username = create_user.username
#     create_user_model.first_name = create_user.first_name
#     create_user_model.last_name = create_user.last_name
#
#     hash_password = bcrypt_context.hash(create_user.password)
#
#     create_user_model.hashed_password = hash_password
#     create_user_model.is_active = True
#
#     db.add(create_user_model)
#     db.commit()


# @router.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
#                                  db: Session = Depends(get_db)):
#     user = authenticate_user(form_data.username, form_data.password, db)
#     if not user:
#         raise token_exception()
#     token_expires = timedelta(minutes=20)
#     token = create_access_token(user.username,
#                                 user.id,
#                                 expires_delta=token_expires)
#     return {"token": token}
