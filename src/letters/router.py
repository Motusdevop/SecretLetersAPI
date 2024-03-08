from database import LetterOrm
from fastapi import APIRouter, HTTPException
from letters.repository import LetterRepository
from letters.schemas import Password, SLetter, SNewLetter
from letters.utils import generate_token

router = APIRouter(prefix='/letters')

@router.get('/get/{token}')
async def get_letter(token: str, password: Password) -> SLetter:

    letter: LetterOrm | None = await LetterRepository.find(token=token)

    if letter is None:
        raise HTTPException(status_code=404, detail="Invalid Token")
    
    if password.password == letter.password:
        await LetterRepository.delete_letter(token)

        return letter
    else:
        raise HTTPException(status_code=401, detail="Wrong Token or Password")

@router.post('/new')
async def new_letter(new_letter: SNewLetter) -> dict:
    token: str = generate_token()

    letter = SLetter(**new_letter.model_dump(), token=token, id=None)

    await LetterRepository.add(letter)

    return {"token": token}