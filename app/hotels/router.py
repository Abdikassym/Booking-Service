
from app.hotels.schemas import SHotels
from fastapi import APIRouter
from app.hotels.dao import HotelsDAO
from datetime import date


router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)


@router.get("/")
async def get_hotels_by_location_and_time(location, date_from: date, date_to: date):
    return await HotelsDAO.find_by_location_and_time(location=location, date_from=date_from, date_to=date_to)


@router.get("/hotels_by_location")
async def get_hotels_by_location(location) -> list[SHotels]:
    return await HotelsDAO.find_all(location=location)


@router.get("/id/{hotels_id}")
async def get_hotel_by_id(hotels_id: int) -> SHotels:
    return await HotelsDAO.find_by_id(model_id=hotels_id)
