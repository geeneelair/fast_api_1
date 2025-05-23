import uvicorn
from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Базы больше нет(')
    await create_tables()
    print('База на месте')
    yield
    print('Выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)