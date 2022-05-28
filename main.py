from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def Index():
    return {"msg": "hello world"}


@app.get('/articles/{id}')
def get_article(id: int):
    return {"article": {id}}
