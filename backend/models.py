# # # from sqlalchemy import Column, Integer, String, Text, Float, DateTime
# # # from database import Base
# # # from datetime import datetime


# # # class Trip(Base):

# # #     __tablename__ = "trips"

# # #     id = Column(Integer, primary_key=True, index=True)

# # #     title = Column(String(200), nullable=False)

# # #     category = Column(String(100))

# # #     route = Column(String(500))

# # #     image = Column(String(500))

# # #     rating = Column(Float, default=0)

# # #     reviews = Column(Integer, default=0)

# # #     price = Column(Float)

# # #     duration = Column(String(100))

# # #     difficulty = Column(String(50))

# # #     description = Column(Text)

# # #     tags = Column(String(500))

# # #     recommended_for = Column(String(500))

# # #     ai_match = Column(Integer, default=0)

# # # # ==========================================
# # # # USER MODEL
# # # # ==========================================

# # # class User(Base):

# # #     __tablename__ = "users"

# # #     id = Column(
# # #         Integer,
# # #         primary_key=True,
# # #         index=True
# # #     )

# # #     full_name = Column(
# # #         String(100),
# # #         nullable=False
# # #     )

# # #     email = Column(
# # #         String(150),
# # #         unique=True,
# # #         nullable=False,
# # #         index=True
# # #     )

# # #     profile_image = Column(
# # #         String(500),
# # #         nullable=True
# # #     )   

# # #     profile_image = Column(String(500), nullable=True)

# # #     created_at = Column(
# # #         DateTime,
# # #         default=datetime.utcnow
# # #     )

# # from sqlalchemy import Column, Integer, String, Text, Float, DateTime , ForeignKey
# # from database import Base
# # from datetime import datetime


# # class Trip(Base):
# #     __tablename__ = "trips"

# #     id = Column(Integer, primary_key=True, index=True)

# #     title = Column(String(200), nullable=False)
# #     category = Column(String(100))
# #     route = Column(String(500))
# #     image = Column(String(500))
# #     rating = Column(Float, default=0)
# #     reviews = Column(Integer, default=0)
# #     price = Column(Float)
# #     duration = Column(String(100))
# #     difficulty = Column(String(50))
# #     description = Column(Text)
# #     tags = Column(String(500))
# #     recommended_for = Column(String(500))
# #     ai_match = Column(Integer, default=0)


# # # ==========================================
# # # USER MODEL
# # # ==========================================

# # class User(Base):
# #     __tablename__ = "users"

# #     id = Column(
# #         Integer,
# #         primary_key=True,
# #         index=True
# #     )

# #     full_name = Column(
# #         String(100),
# #         nullable=False
# #     )

# #     email = Column(
# #         String(150),
# #         unique=True,
# #         nullable=False,
# #         index=True
# #     )

# #     # IMPORTANT: Store hashed password
# #     password_hash = Column(
# #         String(255),
# #         nullable=False
# #     )

# #     profile_image = Column(
# #         String(500),
# #         nullable=True
# #     )

# #     created_at = Column(
# #         DateTime,
# #         default=datetime.utcnow
# #     )

# # # =========================================================
# # # AI DESTINATION MODEL
# # # =========================================================

# # class Destination(Base):
# #     __tablename__ = "destinations"

# #     id = Column(Integer, primary_key=True, index=True)

# #     name = Column(String(150), nullable=False)

# #     district = Column(String(100))

# #     category = Column(String(150))

# #     description = Column(Text)

# #     best_for = Column(String(500))

# #     tags = Column(String(500))

# #     average_stay = Column(Integer, default=2)

# #     base_cost_per_person = Column(Float, default=0)

# #     hotel_cost_per_night = Column(Float, default=0)

# #     food_cost_per_day = Column(Float, default=0)

# #     transport_cost = Column(Float, default=0)

# #     rating = Column(Float, default=0)

# #     image = Column(String(500), nullable=True)

# #     latitude = Column(Float, nullable=True)

# #     longitude = Column(Float, nullable=True)

# # # =========================================================
# # # AI TRANSPORT COST MODEL
# # # =========================================================

# # class TravelCost(Base):
# #     __tablename__ = "travel_costs"

# #     id = Column(Integer, primary_key=True, index=True)

# #     destination = Column(
# #         String(150),
# #         nullable=False
# #     )

# #     transport_type = Column(
# #         String(50),
# #         nullable=False
# #     )

# #     estimated_cost = Column(
# #         Float,
# #         default=0
# #     )

# #     duration_hours = Column(
# #         Float,
# #         default=0
# #     )

# #     comfort_level = Column(
# #         String(50)
# #     )

# # # =========================================================
# # # AI FOOTFALL MODEL
# # # =========================================================

# # class FootfallData(Base):
# #     __tablename__ = "footfall_data"

# #     id = Column(Integer, primary_key=True, index=True)

# #     destination = Column(
# #         String(150),
# #         nullable=False
# #     )

# #     visit_date = Column(
# #         DateTime,
# #         nullable=False
# #     )

# #     crowd_level = Column(
# #         String(50),
# #         nullable=False
# #     )

# #     crowd_score = Column(
# #         Integer,
# #         default=50
# #     )

# #     estimated_visitors = Column(
# #         Integer,
# #         default=0
# #     )

# # # ///////////////////////////////HOTELS///////////////////////////////////
# # class Hotel(Base):

# #     __tablename__ = "hotels"

# #     id = Column(
# #         Integer,
# #         primary_key=True,
# #         index=True
# #     )

# #     trip_id = Column(
# #         Integer,
# #         ForeignKey("trips.id"),
# #         nullable=False
# #     )

# #     name = Column(
# #         String(200),
# #         nullable=False
# #     )

# #     location = Column(
# #         String(200)
# #     )

# #     image = Column(
# #         String(500)
# #     )

# #     rating = Column(
# #         Float
# #     )

# #     price_per_night = Column(
# #         Float
# #     )

# #     room_type = Column(
# #         String(100)
# #     )

# #     facilities = Column(
# #         Text
# #     )

# #     available_rooms = Column(
# #         Integer,
# #         default=0
# #     )

# #     description = Column(
# #         Text
# #     )

# from database import SessionLocal, engine, Base
# from models import Trip, Hotel


# # Create tables if they don't exist

# Base.metadata.create_all(
#     bind=engine
# )


# # Open ONE database session

# db = SessionLocal()


# try:

#     # ==================================================
#     # ORIGINAL TRIPS
#     # ==================================================

#     trips = [

#         # Your existing Trip(...) objects here

#     ]


#     # Insert original trips only if they don't exist

#     for trip in trips:

#         existing = (
#             db.query(Trip)
#             .filter(
#                 Trip.title == trip.title
#             )
#             .first()
#         )

#         if not existing:

#             db.add(trip)


#     db.commit()


#     # ==================================================
#     # NEW TRIPS
#     # ==================================================

#     new_trips = [

#         Trip(
#             title="Dooars Forest Escape",
#             category="Wildlife",
#             route="Lataguri → Jaldapara → Buxa",
#             image="assets/img4.jpeg",
#             rating=4.7,
#             reviews=140,
#             price=7200,
#             duration="4 Days / 3 Nights",
#             difficulty="Moderate",
#             description="Explore the forests, wildlife and rivers of Dooars.",
#             tags="Wildlife,Nature,Adventure",
#             recommended_for="Nature Lovers, Families",
#             ai_match=92
#         ),

#         Trip(
#             title="Kalimpong Mountain Escape",
#             category="Mountains",
#             route="Siliguri → Kalimpong → Lava",
#             image="assets/img5.jpeg",
#             rating=4.6,
#             reviews=118,
#             price=6800,
#             duration="4 Days / 3 Nights",
#             difficulty="Easy",
#             description="Enjoy peaceful mountain landscapes and beautiful Himalayan views.",
#             tags="Mountains,Photography,Nature",
#             recommended_for="Couples, Photographers",
#             ai_match=90
#         ),

#         Trip(
#             title="Digha Coastal Escape",
#             category="Beach",
#             route="Kolkata → Digha → Mandarmani",
#             image="assets/img6.jpeg",
#             rating=4.4,
#             reviews=210,
#             price=5200,
#             duration="3 Days / 2 Nights",
#             difficulty="Easy",
#             description="Relax beside the sea and explore the beautiful coastal side of Bengal.",
#             tags="Beach,Relaxation,Food",
#             recommended_for="Families,Couples",
#             ai_match=88
#         ),

#         Trip(
#             title="Sundarbans Adventure",
#             category="Wildlife",
#             route="Kolkata → Gosaba → Sundarbans",
#             image="assets/img7.jpeg",
#             rating=4.8,
#             reviews=175,
#             price=8500,
#             duration="4 Days / 3 Nights",
#             difficulty="Moderate",
#             description="Experience mangrove forests, rivers and unique wildlife in the Sundarbans.",
#             tags="Wildlife,Nature,Adventure",
#             recommended_for="Adventure Lovers,Wildlife Lovers",
#             ai_match=95
#         )

#     ]


#     # Insert new trips only if they don't exist

#     for trip in new_trips:

#         existing = (
#             db.query(Trip)
#             .filter(
#                 Trip.title == trip.title
#             )
#             .first()
#         )

#         if not existing:

#             db.add(trip)


#     db.commit()


#     # ==================================================
#     # FIND DOOARS
#     # ==================================================

#     dooars = (
#         db.query(Trip)
#         .filter(
#             Trip.title == "Dooars Forest Escape"
#         )
#         .first()
#     )


#     if not dooars:

#         raise Exception(
#             "Dooars Forest Escape was not found."
#         )


#     # ==================================================
#     # DOOARS HOTELS
#     # ==================================================

#     dooars_hotels = [

#         Hotel(
#             trip_id=dooars.id,
#             name="Dooars Retreat",
#             location="Lataguri",
#             image="assets/hotel1.jpeg",
#             rating=4.5,
#             price_per_night=2500,
#             room_type="Deluxe Room",
#             facilities="WiFi,Breakfast,Parking,AC",
#             available_rooms=5,
#             description="Comfortable stay surrounded by the forests of Dooars."
#         ),

#         Hotel(
#             trip_id=dooars.id,
#             name="Forest View Resort",
#             location="Lataguri",
#             image="assets/hotel2.jpeg",
#             rating=4.7,
#             price_per_night=3200,
#             room_type="Premium Room",
#             facilities="WiFi,Pool,Breakfast,Parking",
#             available_rooms=3,
#             description="A peaceful resort with beautiful forest views."
#         )

#     ]


#     # Insert hotels only if they don't already exist

#     for hotel in dooars_hotels:

#         existing = (
#             db.query(Hotel)
#             .filter(
#                 Hotel.name == hotel.name,
#                 Hotel.trip_id == hotel.trip_id
#             )
#             .first()
#         )


#         if not existing:

#             db.add(hotel)


#     db.commit()


#     print(
#         "Trips and hotels inserted successfully."
#     )


# except Exception as error:

#     db.rollback()

#     print(
#         "Seed failed:",
#         error
#     )

#     raise


# finally:

#     db.close()

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey
)

from database import Base

from datetime import datetime


# =========================================================
# TRIP MODEL
# =========================================================

class Trip(Base):

    __tablename__ = "trips"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200),
        nullable=False
    )

    category = Column(
        String(100)
    )

    route = Column(
        String(500)
    )

    image = Column(
        String(500)
    )

    rating = Column(
        Float,
        default=0
    )

    reviews = Column(
        Integer,
        default=0
    )

    price = Column(
        Float
    )

    duration = Column(
        String(100)
    )

    difficulty = Column(
        String(50)
    )

    description = Column(
        Text
    )

    tags = Column(
        String(500)
    )

    recommended_for = Column(
        String(500)
    )

    ai_match = Column(
        Integer,
        default=0
    )


# =========================================================
# USER MODEL
# =========================================================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    profile_image = Column(
        String(500),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# =========================================================
# AI DESTINATION MODEL
# =========================================================

class Destination(Base):

    __tablename__ = "destinations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(150),
        nullable=False
    )

    district = Column(
        String(100)
    )

    category = Column(
        String(150)
    )

    description = Column(
        Text
    )

    best_for = Column(
        String(500)
    )

    tags = Column(
        String(500)
    )

    average_stay = Column(
        Integer,
        default=2
    )

    base_cost_per_person = Column(
        Float,
        default=0
    )

    hotel_cost_per_night = Column(
        Float,
        default=0
    )

    food_cost_per_day = Column(
        Float,
        default=0
    )

    transport_cost = Column(
        Float,
        default=0
    )

    rating = Column(
        Float,
        default=0
    )

    image = Column(
        String(500),
        nullable=True
    )

    latitude = Column(
        Float,
        nullable=True
    )

    longitude = Column(
        Float,
        nullable=True
    )


# =========================================================
# AI TRANSPORT COST MODEL
# =========================================================

class TravelCost(Base):

    __tablename__ = "travel_costs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    destination = Column(
        String(150),
        nullable=False
    )

    transport_type = Column(
        String(50),
        nullable=False
    )

    estimated_cost = Column(
        Float,
        default=0
    )

    duration_hours = Column(
        Float,
        default=0
    )

    comfort_level = Column(
        String(50)
    )


# =========================================================
# AI FOOTFALL MODEL
# =========================================================

class FootfallData(Base):

    __tablename__ = "footfall_data"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    destination = Column(
        String(150),
        nullable=False
    )

    visit_date = Column(
        DateTime,
        nullable=False
    )

    crowd_level = Column(
        String(50),
        nullable=False
    )

    crowd_score = Column(
        Integer,
        default=50
    )

    estimated_visitors = Column(
        Integer,
        default=0
    )


# =========================================================
# HOTEL MODEL
# =========================================================

class Hotel(Base):

    __tablename__ = "hotels"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    trip_id = Column(
        Integer,
        ForeignKey("trips.id"),
        nullable=False
    )

    name = Column(
        String(200),
        nullable=False
    )

    location = Column(
        String(200)
    )

    image = Column(
        String(500)
    )

    rating = Column(
        Float
    )

    price_per_night = Column(
        Float
    )

    room_type = Column(
        String(100)
    )

    facilities = Column(
        Text
    )

    available_rooms = Column(
        Integer,
        default=0
    )

    description = Column(
        Text
    )