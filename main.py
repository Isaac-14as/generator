import asyncio
import datetime
import random
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, delete, insert, select, update, text

DB_HOST='localhost'
DB_PORT='5432'
DB_USER='postgres'
DB_PASS='postgres'
DB_NAME='diploma_db'



DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


async_engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

class ValueDevice(Base):
    __tablename__ = 'value_device'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_power: Mapped[float | None]
    active_power: Mapped[float | None]
    reactive_power: Mapped[float | None]
    voltage: Mapped[float | None]
    amperage: Mapped[float | None]
    power_factor: Mapped[float | None]
    date_of_collection: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    device_id: Mapped[int]



async def add(data):
    async with async_session_maker() as session:

        query = insert(ValueDevice).values(**data)
        await session.execute(query)
        await session.commit()

# async def add():
#     async with async_engine.connect() as conn:
#         stmt = """insert into value_device (full_power, active_power, reactive_power, voltage, amperage, power_factor, device_id) values (10, 10, 10, 10, 10, 10, 1)"""
#         # stmt = """select * from device"""
#         await conn.execute(text(stmt))
#         await conn.commit()


# async def time_sleap():
#     await asyncio.sleep(2)  # Имитация асинхронной операции


async def print_numbers():

    while True:
        data = {
            'full_power': round(random.uniform(2, 20), 2),
            'active_power': round(random.uniform(2, 20), 2),
            'reactive_power': round(random.uniform(2, 20), 2),
            'voltage': round(random.uniform(2, 20), 2),
            'amperage': round(random.uniform(2, 20), 2),
            'power_factor': round(random.uniform(0, 1), 2),
            'device_id': 1
        }
        await add(data)
        data = {
            'full_power': round(random.uniform(2, 20), 2),
            'active_power': round(random.uniform(2, 20), 2),
            'reactive_power': round(random.uniform(2, 20), 2),
            'voltage': round(random.uniform(2, 20), 2),
            'amperage': round(random.uniform(2, 20), 2),
            'power_factor': round(random.uniform(0, 1), 2),
            'device_id': 2
        }
        await add(data)
        data = {
            'full_power': round(random.uniform(2, 20), 2),
            'active_power': round(random.uniform(2, 20), 2),
            'reactive_power': round(random.uniform(2, 20), 2),
            'voltage': round(random.uniform(2, 20), 2),
            'amperage': round(random.uniform(2, 20), 2),
            'power_factor': round(random.uniform(0, 1), 2),
            'device_id': 3
        }
        await add(data)
        data = {
            'full_power': round(random.uniform(2, 20), 2),
            'active_power': round(random.uniform(2, 20), 2),
            'reactive_power': round(random.uniform(2, 20), 2),
            'voltage': round(random.uniform(2, 20), 2),
            'amperage': round(random.uniform(2, 20), 2),
            'power_factor': round(random.uniform(0, 1), 2),
            'device_id': 4
        }
        await add(data)
        await asyncio.sleep(3)

async def main():
    task = asyncio.create_task(print_numbers())
    await task

asyncio.run(main())