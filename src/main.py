import uvicorn
from fastapi import FastAPI

from letters.router import router as letters_router

app = FastAPI()

app.include_router(letters_router)

@app.get("/")
async def index():
    return {'data': 'Hello World!'}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)