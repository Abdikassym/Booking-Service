from datetime import date, datetime
from fastapi import APIRouter, Depends, Request
from pydantic import parse_obj_as

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking
from app.exceptions import RoomCannotBeBookedException
from app.tasks.tasks import send_booking_confirmation
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingsDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user)
):
    booking = await BookingsDAO.add(user_id=user.id, room_id=room_id, date_from=date_from, date_to=date_to)
    booking_dict = parse_obj_as(SBooking, booking)
    
    if not booking:
        raise RoomCannotBeBookedException
    send_booking_confirmation(booking_dict, user.email)
    return booking_dict

@router.delete("/{booking_id}")
async def delete_booking(
    booking_id: int,
    user: Users = Depends(get_current_user)
    ):  
    return await BookingsDAO.delete_by_id(booking_id)