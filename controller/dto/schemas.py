from pydantic import BaseModel


class ArticleSchema(BaseModel):
    id: int
    title: str
    desciption: str
