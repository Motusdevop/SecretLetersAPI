from pydantic import BaseModel

class SNewLetter(BaseModel):
    title: str
    password: str
    body: str | None
    author: str | None

class SLetter(SNewLetter):
    token: str

class Password(BaseModel):
    password: str