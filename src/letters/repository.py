from database import LetterOrm, async_session_factory
from letters.schemas import SLetter
from sqlalchemy import delete, select


class LetterRepository:

    @classmethod
    async def add(cls, data: SLetter) -> str:
        async with async_session_factory() as session:
            data_dict = data.model_dump()

            letter = LetterOrm(**data_dict)

            session.add(letter)
            await session.commit()
    
    @classmethod
    async def find(cls, token: str):
        async with async_session_factory() as session:
            query = select(LetterOrm).where(LetterOrm.token == token)
            result = await session.execute(query)
            letter_model = result.scalars().one_or_none()
            print(f'{type(letter_model)=}')
            print(f'{letter_model=}')
            return letter_model
        
    @classmethod
    async def delete_letter(cls, token: str):
        async with async_session_factory() as session:
            query = delete(LetterOrm).where(LetterOrm.token == token)
            await session.execute(query)
            await session.commit()


