from uuid import uuid4
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, DOUBLE
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dbsession import Base


class Cities(Base):
    __tablename__ = 'cities'
    city_id: Mapped[int] = mapped_column(primary_key=True)
    nation_id: Mapped[int]
    state_id: Mapped[int]
    name: Mapped[str] = mapped_column(String(100))
    abbreviation: Mapped[str] = mapped_column(String(10))
    latitude: Mapped[float] = mapped_column(DOUBLE)
    longitude: Mapped[float] = mapped_column(DOUBLE)

    def __repr__(self) -> str:
        return f"City(id={self.city_id!r}, name={self.name!r}, abbreviation={self.abbreviation!r})"

    # @classmethod
    # async def create(cls, db: AsyncSession, city_id=None, **kwargs):
    #     if not city_id:
    #         city_id = uuid4().hex
    #     transaction = cls(city_id=city_id, **kwargs)
    #     db.add(transaction)
    #     await db.commit()
    #     await db.refresh(transaction)
    #     return transaction
    #
    # @classmethod
    # async def get(cls, db: AsyncSession, city_id: int):
    #     try:
    #         transaction = await db.get(cls, city_id)
    #     except NoResultFound:
    #         return None
    #     return transaction
    #
    # @classmethod
    # async def get_all(cls, db: AsyncSession):
    #     return (await db.execute(select(cls))).scalars().all()
