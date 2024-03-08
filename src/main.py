from contextlib import asynccontextmanager

import uvicorn
from database import create_tables  # , drop_tables()
from fastapi import FastAPI
from letters.router import router as letters_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Starting')
    # await drop_tables()
    await create_tables()
    print('Success create tables')
    yield
    print('Off and drop tables')
    


app = FastAPI(lifespan=lifespan)

app.include_router(letters_router)

@app.get("/")
async def index():
    return {'data': 'Hello World!'}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)