from datetime import date
from sqlalchemy import and_, func, select
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.database import async_session_maker
from app.rooms.models import Rooms

class HotelsDAO(BaseDAO):

    model = Hotels

    @classmethod
    async def find_all(cls, location: str):
        async with async_session_maker() as session:
            # Получаем отели по локации
            hotel_query = select(cls.model).filter(cls.model.location.ilike(f"%{location}%"))
            hotel_result = await session.execute(hotel_query)
            hotels = hotel_result.scalars().all()
            
            
            # Получаем комнаты для найденных отелей
            room_query = select(Rooms).where(Rooms.hotel_id.in_([hotel.id for hotel in hotels]))
            room_result = await session.execute(room_query)
            all_rooms = room_result.scalars().all()


            # Подсчитываем количество бронирований для каждой комнаты
            booking_query = select(Bookings.room_id, func.count(Bookings.id)).group_by(Bookings.room_id)
            booking_result = await session.execute(booking_query)

            # Извлекаем данные из booking_result
            booking_counts = {}
            for room_id, count in booking_result:
                booking_counts[room_id] = count


             # Фильтруем отели с доступными комнатами
            allowed_hotels = set()
            for room in all_rooms:
                if booking_counts.get(room.id, 0) < room.quantity:
                    allowed_hotels.add(room.hotel_id)
        
            return [hotel for hotel in hotels if hotel.id in allowed_hotels]
        

            
    @classmethod
    async def find_by_location_and_time(cls, location, 
                                        date_from:date, 
                                        date_to: date):

        async with async_session_maker() as session:
            # Получаем отели по локации
            hotel_query = select(Hotels).filter(Hotels.location.ilike(f"%{location}%"))
            hotel_result = await session.execute(hotel_query)
            hotels = hotel_result.scalars().all()

            # Получаем комнаты для найденных отелей
            room_query = select(Rooms).where(Rooms.hotel_id.in_([hotel.id for hotel in hotels]))
            room_result = await session.execute(room_query)
            all_rooms = room_result.scalars().all()

            # Подсчитываем количество бронирований для каждой комнаты
            booking_query = select(Bookings).where(and_(Bookings.date_from <= date_to, Bookings.date_from >= date_from))
            booking_result = await session.execute(booking_query)

            # Извлекаем данные из booking_result
            booking_counts = {}
            for room_id in booking_result:
                if room_id in booking_counts:
                    booking_counts[room_id] += 1
                else:
                    booking_counts[room_id] = 1
                    
            # Фильтруем отели с доступными комнатами
            allowed_hotels = set()
            for room in all_rooms:
                if booking_counts.get(room.id, 0) < room.quantity:
                    allowed_hotels.add(room.hotel_id)

            # Возвращаем отели с доступными комнатами
            return [hotel for hotel in hotels if hotel.id in allowed_hotels]