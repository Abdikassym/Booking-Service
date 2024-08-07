from sqladmin import Admin, ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.rooms.models import Rooms
from app.users.models import Users

class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email, Users.booking]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    column_details_list = [Users.id, Users.email, Users.booking]


class BookingsAdmin(ModelView, model=Bookings):
    column_list = [c.name for c in Rooms.__table__.c] + [Bookings.room]
    name = "Бронь"
    name_plural = "Бронирования"
    icon = "fa-solid fa-calendar"


class RoomsAdmin(ModelView, model=Rooms):
    column_list = [c.name for c in Rooms.__table__.c] + [Rooms.booking, Rooms.hotel]
    name = "Комната"
    name_plural = "Комнаты"
    icon = "fa-solid fa-bed"


class HotelsAdmin(ModelView, model=Hotels):
    column_list = [c.name for c in Hotels.__table__.c] + [Hotels.room]
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-building"
