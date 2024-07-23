from fastapi import FastAPI, Query, Depends

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.rooms.router import router as router_rooms

app = FastAPI(
    title="Something"
)


app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_users)


hotels = [
        {
        "address": "ул.Гагарина 1, Алтай",
        "name": "Super Hotel",
        "stars": 5
        },
    ]
