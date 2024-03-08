from config import settings
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False
)

async_session_factory = async_sessionmaker(async_engine)

class Model(DeclarativeBase):
    pass

class LetterOrm(Model):
    __tablename__ = 'letters'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    password: Mapped[str]
    body: Mapped[str | None]
    author: Mapped[str | None]
    token: Mapped[str | None]

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


# async def drop_tables():
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Model.metadata.drop_all)