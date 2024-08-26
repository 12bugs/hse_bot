from sqlalchemy import String, ForeignKey, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from dotenv import load_dotenv
from config import SQLALCHEMY_URL


load_dotenv()

engine = create_async_engine(SQLALCHEMY_URL)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    tg_id = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    program: Mapped[str] = mapped_column(String(100))
    course: Mapped[str] = mapped_column(String(10))
    tg_name: Mapped[str] = mapped_column(String(50))


class Day(Base):
    __tablename__ = 'days'

    id: Mapped[int] = mapped_column(primary_key=True)
    day_str: Mapped[str] = mapped_column(String(20))


class Time(Base):
    __tablename__ = 'times'

    id: Mapped[int] = mapped_column(primary_key=True)
    hour_str: Mapped[str] = mapped_column(String(10))


class DayTimeUser(Base):
    __tablename__ = 'loans'

    day: Mapped[int] = mapped_column(ForeignKey('days.id'), primary_key=True)
    hour: Mapped[int] = mapped_column(ForeignKey('times.id'), primary_key=True)
    is_free: Mapped[bool] = mapped_column(default=True)
    user = mapped_column(BigInteger, ForeignKey('users.tg_id'), nullable=True)
    need_ball: Mapped[bool] = mapped_column(nullable=True)


class Admin(Base):
    __tablename__ = 'admin'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)