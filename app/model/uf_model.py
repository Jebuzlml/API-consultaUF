from pydantic import BaseModel


class Uf(BaseModel):
    year: str
    month: str
    day: str
