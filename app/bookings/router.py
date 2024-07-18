from sqlalchemy import select
from fastapi import APIRouter

from app.bookings.models import Bookings
from app.database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Bookings)  # SELECT * FROM bookings
        result = await session.execute(query)
        return result.mappings().all()