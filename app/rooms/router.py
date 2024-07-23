from app.hotels.router import router
from app.rooms.dao import RoomsDAO
from fastapi import APIRouter

router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)


@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id: int):
    return await RoomsDAO.find_all(hotel_id=hotel_id)
