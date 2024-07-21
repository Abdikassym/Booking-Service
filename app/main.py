from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date, datetime, timedelta
import jwt
from pydantic import BaseModel
from sqlalchemy import select

from app.bookings.router import router as router_bookings
from app.users.auth import authenticate_user, create_access_token
from app.users.models import Users
from app.users.router import router as router_users

from app.database import async_session_maker
from app.dao.base import BaseDAO

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI(
    title="Something"
)


app.include_router(router_users)
app.include_router(router_bookings)


hotels = [
        {
        "address": "ул.Гагарина 1, Алтай",
        "name": "Super Hotel",
        "stars": 5
        },
    ]

class HotelsSearchArgs():
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            stars: Optional[int] = Query(None, ge=1, le=5),
            has_spa: Optional[bool] = None
            ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


# class SHotel(BaseModel):  
#     address: str
#     name: str
#     stars: int


@app.get("/hotels")
def get_hotels(search_args: HotelsSearchArgs = Depends()):
    return search_args


class SBooking(BaseModel):
    room_id: int = 1
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    hotels.append(booking)
    return hotels