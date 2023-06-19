from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db import get_db

from app.models import Cities as CitiesModel

router = APIRouter(prefix="/cities", tags=["cities"])


class CitiesSchemaBases(BaseModel):
    name: str | None = None
    abbreviation: str | None = None
    latitude: float | None = None
    longitude: float | None = None


class CitiesSchemaCreate(CitiesSchemaBases):
    pass


class CitiesSchema(CitiesSchemaBases):
    city_id: int

    class Config:
        orm_mode = True


@router.get("/get-city", response_model=CitiesSchema)
async def get_city(city_id: int, db: AsyncSession = Depends(get_db)):
    city = await CitiesModel.get(db, city_id)
    return city


@router.get("/get-cities", response_model=list[CitiesSchema])
async def get_cities(db: AsyncSession = Depends(get_db)):
    cities = await CitiesModel.get_all(db)
    return cities


@router.post("/create-city", response_model=CitiesSchema)
async def create_city(city: CitiesSchemaCreate, db: AsyncSession = Depends(get_db)):
    city = await CitiesModel.create(db, **city.dict())
    return city
