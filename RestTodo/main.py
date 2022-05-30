from fastapi import FastAPI
from fastapi_router_controller import ControllersTags

from controller import users_controller

app = FastAPI(
    title='fast api study',
    description='This is a very fancy project, with auto docs for the API and everything',
    version='0.0.1',
    docs_url='/docs',
    openapi_tags=ControllersTags)

app.include_router(users_controller.router)
