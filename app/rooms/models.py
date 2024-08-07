from sqlalchemy import JSON, Column, Date, ForeignKey, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id"))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)

    booking = relationship("Bookings", back_populates="room")
    hotel = relationship("Hotels", back_populates="room")
    
    def __str__(self) -> str:
        return f"{self.name}"