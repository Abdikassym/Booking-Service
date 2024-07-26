from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.rooms.router import router as router_rooms
from app.pages.router import router as router_pages
from app.images.router import router as router_images


app = FastAPI(
    title="Something"
)

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_users)
app.include_router(router_pages)
app.include_router(router_images)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTINONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-cookie", "Access-Control-Allow-Headers", "Authorization", "Access-Control-Allow-Origin"]
)