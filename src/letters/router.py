from fastapi import APIRouter, HTTPException

from database import letters_db

from letters.schemas import Password, SLetter, SNewLetter
from letters.utils import generate_token

router = APIRouter(prefix='/letters')

@router.get('/get/{token}')
def get_letter(token: str, password: Password) -> SLetter:

    try:
        letter: SLetter = letters_db[token]
    except KeyError:
        raise HTTPException(status_code=404, detail="Invalid Token")


    if password.password == letter.password:
        del letters_db[token]
        del letter.password
        del letter.token
        return letter
    else:
        raise HTTPException(status_code=401, detail="Wrong Password")

@router.post('/new')
def new_letter(new_letter: SNewLetter) -> dict:
    token = generate_token()

    letter = SLetter(**new_letter.model_dump(), token=token)

    letters_db[token] = letter

    return {"token": token}