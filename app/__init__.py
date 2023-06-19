from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config import config
from app.db.db import sessionmanager


def init_app(init_db=True):
    lifespan = None

    if init_db:
        sessionmanager.init(config.DBConfig.POSTGRES_DATABASE_URI)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            if sessionmanager._engine is not None:
                await sessionmanager.close()

    server = FastAPI(lifespan=lifespan)
    from app.views.cities import router as city_router
    server.include_router(city_router, prefix="/api/v1", tags=["cities"])
    return server
